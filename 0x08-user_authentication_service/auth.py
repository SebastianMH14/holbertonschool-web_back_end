#!/usr/bin/env python3
"""auth class for authentication"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """returned bytes is a salted hash of the input password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
