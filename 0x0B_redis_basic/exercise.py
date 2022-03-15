#!/usr/bin/env python3
"""
Writing strings to Redis
"""
import redis
import uuid
from typing import Union
from collections.abc import Callable


class Cache:
    """store an instance of the Redis client
    as a private variable named _redis"""

    def __init__(self) -> None:
        """constructor de clase"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store the input data in Redis
        using the random key and return the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn):
        """convert the data back to the desired format"""
        result = self._redis.get(key)
        if result:
            fn.g
        return result

    def get_str(self, str_utf8: str) -> str:
        """convert utf8 to string"""
        return str(str_utf8.decode('utf8'))

    def get_int(self, int_utf8) -> int:
        """convert utf8 to int"""
        return int(int_utf8.decode('utf8'))
