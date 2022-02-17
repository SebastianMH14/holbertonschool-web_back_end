#!/usr/bin/env python3
"""class BasicAuth that inherits from Auth"""
from api.v1.auth.auth import Auth
from base64 import b64decode
from typing import Tuple, TypeVar
from models.user import User


class BasicAuth(Auth):
    """class BasicAuth to basic authentication"""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """returns the Base64 part of the Authorization
        header for a Basic Authentication"""
        if authorization_header is None or type(
                authorization_header) is not str or authorization_header.find(
                    'Basic ') == -1:
            return None
        else:
            return authorization_header.lstrip('Basic ')

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """returns the decoded value of a Base64 string"""
        if base64_authorization_header is None or type(
                base64_authorization_header) is not str:
            return None
        else:
            try:
                decoded = b64decode(base64_authorization_header)
                return decoded.decode('utf-8')
            except Exception as e:
                return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """returns the user email and password from the Base64 decoded value"""
        if decoded_base64_authorization_header is None\
            or type(
                decoded_base64_authorization_header
            ) is not str or decoded_base64_authorization_header.find(
                ':') == -1:
            return (None, None)
        else:
            value = decoded_base64_authorization_header.split(':', 1)
            return (value[0], value[1])

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """returns the User instance based on his email and password."""
        new_user = User()
        if user_email is None or type(user_email) is not str:
            return None
        elif user_pwd is None or type(user_pwd) is not str:
            return None
        try:
            search = User.search({'email': user_email})
            if (len(search) == 0):
                return None
            check_pwd = search[0].is_valid_password(user_pwd)
            if check_pwd is False:
                return None
            return search[0]
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """overloads Auth and retrieves the User instance for a request"""
        header = BasicAuth().authorization_header(request)
        extract_header = self.extract_base64_authorization_header(header)
        decode = self.decode_base64_authorization_header(extract_header)
        extract_user = self.extract_user_credentials(decode)
        return self.user_object_from_credentials(
            extract_user[0], extract_user[1])
