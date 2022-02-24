#!/usr/bin/env python3
"""Flask app"""
from flask import Flask, jsonify, request
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
        return jsonify({"email": "{}".
                        format(email), "message": "user created"}), 400
    except ValueError:
        return jsonify({"message": "email already registered"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
