"""

"""
from pymongo import MongoClient

client = MongoClient()
db = client['weibo']
collection = db['weibo']


def save_to_mongo(result):
    if collection.insert(result):
        print('Saved to Mongo')
