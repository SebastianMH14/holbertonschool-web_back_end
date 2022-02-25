#!/usr/bin/env python3
"""auth class for authentication"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """save the user to the database
        using self._db and return the User object"""
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError('User {} already exists'.format(email))
        except NoResultFound:
            hash_pwd = _hash_password(password)
            return self._db.add_user(email, hash_pwd)

    def valid_login(self, email: str, password: str) -> bool:
        """If it matches return True.
        In any other case, return False."""
        try:
            found_user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode('utf8'),
                              found_user.hashed_password):
                return True
            else:
                return False
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """ It takes an email string argument
        and returns the session ID as a string"""
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            user.session_id = session_id
            self._db._session.commit()
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id) -> User:
        """
        If the session ID is None or no user is found,
        return None. Otherwise return the corresponding user.
        """
        if session_id is None:
            return None
        else:
            try:
                user = self._db.find_user_by(session_id=session_id)
                return user
            except NoResultFound:
                return None

    def destroy_session(self, user_id: int) -> None:
        """updates the corresponding user’s session ID to None"""
        user = self._db.find_user_by(id=user_id)
        user.session_id = None

    def get_reset_password_token(self, email: str) -> str:
        """generate a UUID and update the user’s
        reset_token database field. Return the token."""
        try:
            user = self._db.find_user_by(email=email)
            reset_token = _generate_uuid()
            user.reset_token = reset_token
            self._db._session.commit()
            return reset_token
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """ hash the password and update the user’s
        hashed_password field with the new hashed
        password and the reset_token field to None"""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hash_pwd = _hash_password(password)
            self._db.update_user(
                user.id, hashed_password=hash_pwd, reset_token=None)
        except NoResultFound:
            raise ValueError


def _hash_password(password: str) -> bytes:
    """returned bytes is a salted hash of the input password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """return a string representation of a new UUID"""
    return str(uuid.uuid4())
