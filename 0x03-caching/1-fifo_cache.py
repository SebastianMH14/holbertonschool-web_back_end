#!/usr/bin/env python3
"""class FIFOCache that inherits from BaseCaching and is a caching system"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """use self.cache_data - dictionary from the parent class BaseCaching"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary
        self.cache_data the item
        value for the key key"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                keys = []
                for k in self.cache_data:
                    keys.append(k)
                self.cache_data.pop(keys[0])
                print("DISCARD: {}".format(keys[0]))
            self.cache_data.update({key: item})

    def get(self, key):
        """return the value in self.cache_data linked to key."""
        if key is None and key in self.cache_data:
            return None
        return self.cache_data.get(key)
