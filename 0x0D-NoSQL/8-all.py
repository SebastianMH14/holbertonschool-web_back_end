#!/usr/bin/env python3
"""Lists all documents in a collection"""


def list_all(mongo_collection):
    """list_all documents"""
    return mongo_collection.find()
