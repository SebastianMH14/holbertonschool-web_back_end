#!/usr/bin/env python3
"""auth class for authentication"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


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


def _hash_password(password: str) -> bytes:
    """returned bytes is a salted hash of the input password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
