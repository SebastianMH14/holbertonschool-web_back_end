#!/usr/bin/env python3
"""Auth class for basic authentication and authorization"""
from flask import request
from typing import List, TypeVar
import os


class Auth:
    """Auth class for authentication and authorization"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns True if the path is not in the
        list of strings excluded_paths"""
        true_or_false = True
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return true_or_false
        else:
            for paths in excluded_paths:
                if paths.replace('/', '') == path.replace('/', ''):
                    true_or_false = False
        return true_or_false

    def authorization_header(self, request=None) -> str:
        """If request doesn't contain the header key Authorization,
        returns None; Otherwise, return the value of the
        header request Authorization"""
        if request is None:
            return None
        else:
            header_auth = request.headers.get('Authorization')
            if header_auth is None:
                return None
            else:
                return header_auth

    def current_user(self, request=None) -> TypeVar('User'):
        """request will be the Flask request object"""
        return None

    def session_cookie(self, request=None):
        """returns a cookie value from a request"""
        if request is None:
            return None
        cookie = os.getenv("SESSION_NAME")
        return request.cookies.get(cookie)
