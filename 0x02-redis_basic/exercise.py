#!/usr/bin/env python3

import redis
import uuid

class Cache:
    '''Represents an object for storing data in a Redis data storage.
    '''
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb(True)
        
    def store(self, data):
        """
        store the input data in Redis using the random key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
