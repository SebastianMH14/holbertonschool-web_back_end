#!/usr/bin/env python3
"""
Writing strings to Redis
"""
import redis
import uuid
from typing import Union
from collections.abc import Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """counts calls to cache"""
    @wraps(method)
    def wrapper(self, *args, **kwds):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


class Cache:
    """store an instance of the Redis client
    as a private variable named _redis"""

    def __init__(self) -> None:
        """constructor de clase"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store the input data in Redis
        using the random key and return the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[
            str, bytes, int, float]:
        """convert the data back to the desired format"""
        result = self._redis.get(key)
        if fn:
            return fn(result)
        return result

    def get_str(self, key: str) -> str:
        """convert utf8 to string"""
        return str(self._redis.get(key).decode("utf-8"))

    def get_int(self, key: str) -> int:
        """convert utf8 to int"""
        return int(self._redis.get(key).decode('utf8'))
