#!/usr/bin/env python3
"""function that inserts a new document
in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """inserts into school collection"""
    mongo_collection.insert_many([kwargs])
    return mongo_collection.find_one({"name": kwargs.get('name')}).get('_id')
