"""

"""
import pymongo

results = collection.find().sort('name', pymongo.ASCENDING).skip(2)
print([result['name'] for result in results])

results = collection.find().sort('name', pymongo.ASCENDING).skip(2).limit(2)
print([result['name'] for result in results])
