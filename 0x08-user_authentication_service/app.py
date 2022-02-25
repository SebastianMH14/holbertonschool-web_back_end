#!/usr/bin/env python3
"""Flask app"""
from flask import Flask, jsonify, request, abort, redirect, url_for
from sqlalchemy import true
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/')
def index():
    """basic route to test"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def register_user():
    """route to register user"""
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """login users and create session and storage id in cookies"""
    email = request.form.get('email')
    password = request.form.get('password')
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        out = jsonify({"email": email, "message": "logged in"})
        out.set_cookie("session_id", session_id)
        return out
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """If the user exists destroy the
    session and redirect the user to GET /"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user is not None:
        AUTH.destroy_session(user.id)
        return redirect(url_for('index'))
    else:
        abort(403)


@app.route('/profile', strict_slashes=False)
def profile():
    """find the user. If the user exist,
    respond with a 200 HTTP"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user is not None:
        email = user.email
        return jsonify({"email": email})
    else:
        abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def reset_password():
    """generate token to reset password"""
    email = request.form.get('email')
    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token}), 200
    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password():
    """If the token is valid update the password."""
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')

    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
