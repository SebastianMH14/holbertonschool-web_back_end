#!/usr/bin/env python3
"""script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


client = MongoClient('mongodb://127.0.0.1:27017')
db = client.logs.nginx
get = [i for i in db.find({"method": "GET"})]
post = [i for i in db.find({"method": "POST"})]
put = [i for i in db.find({"method": "PUT"})]
patch = [i for i in db.find({"method": "PATCH"})]
delete = [i for i in db.find({"method": "DELETE"})]
status = [i for i in db.find({"method": "GET", "path": "/status"})]


print(f'{db.count_documents({})} logs')
print("Methods:")
print(f'\tmethod GET: {len(get)}')
print(f'\tmethod POST: {len(post)}')
print(f'\tmethod PUT: {len(put)}')
print(f'\tmethod PATCH: {len(patch)}')
print(f'\tmethod DELETE: {len(delete)}')
print(f'{len(status)} status check')
