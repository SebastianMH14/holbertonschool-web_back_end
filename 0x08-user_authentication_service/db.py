#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import Base, User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """add new user to the database
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """ takes in arbitrary keyword arguments
        and returns the first row found in the
        users table as filtered by the method's input arguments"""
        if kwargs is None:
            raise InvalidRequestError
        user_found = self._session.query(User).filter_by(**kwargs).first()
        if user_found is None:
            raise NoResultFound
        return user_found

    def update_user(self, user_id: int, **kwargs) -> None:
        """The method will use find_user_by
        """
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if key not in user.__dict__.keys():
                raise ValueError
            else:
                setattr(user, key, value)
        return None
