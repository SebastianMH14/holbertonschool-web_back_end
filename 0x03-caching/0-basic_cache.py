#!/usr/bin/env python3
"""class BasicCache that inherits
from BaseCaching and is a caching system"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """use self.cache_data - dictionary from the parent class BaseCaching
This caching system doesn`t have limit"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary
        self.cache_data the item value
        for the key key."""
        if key and item:
            self.cache_data.update({key: item})

    def get(self, key):
        """return the value in self.cache_data linked to key."""
        if key is None and key in self.cache_data:
            return None
        return self.cache_data.get(key)
