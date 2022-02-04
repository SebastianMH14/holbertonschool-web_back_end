#!/usr/bin/python3
"""class LRUCache that inherits from BaseCaching and is a caching system"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """use self.cache_data - dictionary from the parent class BaseCaching"""

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """assign to the dictionary
        self.cache_data the item
        value for the key key"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.cache_data.popitem(last=False)
                print("DISCARD: {}".format(key))
            self.cache_data.update({key: item})
            self.cache_data.move_to_end(key)

    def get(self, key):
        """return the value in self.cache_data linked to key."""
        if key is None and key in self.cache_data:
            return None
        return self.cache_data.get(key)
