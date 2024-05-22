#!/usr/bin/env python3
""" BasicCache module """
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """ BasicCache class inherits from BaseCaching and implements a simple
        caching system with no limit.
    """

    def put(self, key, item):
        """ Add an item in the cache
            If key or item is None, this method should not do anything.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
            Return the value in self.cache_data linked to key.
            If key is None or if the key doesn’t exist in self.cache_data,
            return None.
        """
        if key is None:
            return None
        return self.cache_data.get(key)

class BaseCaching:
    """ BaseCaching defines:
      - A class constructor that initializes the cache_data dictionary
    """
    def __init__(self):
        """ Initialize the cache """
        self.cache_data = {}
