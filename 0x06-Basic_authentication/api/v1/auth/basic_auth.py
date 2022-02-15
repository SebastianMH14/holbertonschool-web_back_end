#!/usr/bin/env python3
"""class BasicAuth that inherits from Auth"""
from api.v1.auth.auth import Auth


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
