#!/usr/bin/env python3
"""class SessionAuth that inherits from Auth"""
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """creating a new authentication mechanism"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Generate a Session ID,
        Use this Session ID as key of the dictionary
        user_id_by_session_id  the value for this key must be user_id"""
        if user_id is None or type(user_id) is not str:
            return None
        else:
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns a User ID based on a Session ID"""
        if session_id is None or type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ returns a User instance based on a cookie value"""
        id = self.session_cookie(request)
        user = self.user_id_for_session_id(id)
        new_user = User.get(user)
        return new_user

    def destroy_session(self, request=None):
        """deletes the user session / logout"""
        if request is None:
            return False

        cookie = self.session_cookie(request)
        if self.session_cookie(request) is None:
            return False

        user_id = self.user_id_for_session_id(cookie)
        if user_id is None:
            return None

        del self.user_id_by_session_id[cookie]
        return True
