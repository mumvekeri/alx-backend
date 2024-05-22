#!/usr/bin/env python3
""" LFUCache module """
from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """ LFUCache class inherits from BaseCaching and implements an LFU
        caching system with LRU tie-breaking.
    """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.freq = defaultdict(int)
        self.order = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
            If key or item is None, this method should not do anything.
            If the cache exceeds MAX_ITEMS, discard the least frequently used item.
            If there is a tie, discard the least recently used item.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.freq[key] += 1
            self.order.move_to_end(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used key
                lfu_key = min(self.freq, key=lambda k: (self.freq[k], self.order[k]))
                self.order.pop(lfu_key)
                self.freq.pop(lfu_key)
                self.cache_data.pop(lfu_key)
                print(f"DISCARD: {lfu_key}")

            self.cache_data[key] = item
            self.freq[key] = 1
            self.order[key] = None

    def get(self, key):
        """ Get an item by key
            Return the value in self.cache_data linked to key.
            If key is None or if the key doesn’t exist in self.cache_data,
            return None.
        """
        if key is None or key not in self.cache_data:
            return None
        self.freq[key] += 1
        self.order.move_to_end(key)
        return self.cache_data[key]


class BaseCaching:
    """ BaseCaching defines:
      - A class constructor that initializes the cache_data dictionary
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize the cache """
        self.cache_data = {}
