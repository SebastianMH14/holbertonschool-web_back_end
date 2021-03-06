#!/usr/bin/env python3
"""handles all routes for the Session authentication"""
from api.v1.views import app_views
from flask import abort, jsonify, request, session
from models.user import User
import os
from api.v1.app import auth


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """retrieve the User instance based on the email"""
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None or email is False:
        return jsonify({"error": "email missing"}), 400
    if password is None or password is False:
        return jsonify({"error": "password missing"}), 400

    search = User.search({'email': email})
    if len(search) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    if search[0].is_valid_password(password) is False:
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(search[0].id)
    out = jsonify(search[0].to_json())
    out.set_cookie(os.getenv('SESSION_NAME'), session_id)
    return out


@app_views.route('/auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
def logout():
    """deletes the user session / logout"""
    if auth.destroy_session(request) is False:
        abort(404)
    else:
        return jsonify({}), 200
