#!/usr/bin/env python3
"""Module task 14
"""
from operator import itemgetter


def top_students(mongo_collection):
    """Function that returns all students sorted by average score
    """

    list_docs = []
    for doc in mongo_collection.find({}):
        count = 0
        for item in doc['topics']:
            count += item['score']
        doc['averageScore'] = count / len(doc['topics'])
        list_docs.append(doc)

    output = sorted(list_docs, key=itemgetter('averageScore'), reverse=True)
    return output
