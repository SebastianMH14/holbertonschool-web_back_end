#!/usr/bin/env python3
""" Module named session_exp_auth to the class SessionAuth """


from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """ Class to add an expiration date to a Session ID. """
    def __init__(self):
        """ Overload method constructor """
        try:
            self.session_duration = int(getenv('SESSION_DURATION'))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """ Create a Session ID. """
        try:
            new_session_id = super().create_session(user_id)
        except Exception:
            return None

        dict_session = {
            'user_id': user_id,
            'created_at': datetime.now()
        }

        self.user_id_by_session_id[new_session_id] = dict_session
        return new_session_id

    def user_id_for_session_id(self, session_id=None):
        """ Method that return user id for session id """
        if session_id is None:
            return None

        this_session = self.user_id_by_session_id.get(session_id)
        if this_session is None:
            return None

        if self.session_duration <= 0:
            return this_session.get('user_id')

        this_session_created = this_session.get('created_at')
        if this_session_created is None:
            return None

        if this_session_created is None or this_session_created + timedelta(
                seconds=self.session_duration) < datetime.now():
            return None

        return this_session.get('user_id')
