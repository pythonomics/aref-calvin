# The Mongo database is currently only accessible on the localhost.
# I will try to publish a public webpage using Amazon Web Services tomorrow. 

import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 4444)

db = client.firstdb

users = db.users
users_data = {
        'username': 'Ting',
        'password': 'ting123',
}

result = users.insert_one(users_data)
print("One post:{0}".format(result.inserted_id))

print "Done" 
