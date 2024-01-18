import os
from pymongo import MongoClient

# Replace the uri string with your MongoDB deployment's connection string
uri = os.environ.get('MONGODB_CONNECTION_STRING')
print("Connection to the MongoDB has been successful !!!")

client = MongoClient(uri)

# database and collection code goes here
db = client.gds_db
print(f"You are using {db} DB")
coll = db.airbnb_revies
print(f"colleciton is {coll}")

# find code goes here
cursor = coll.find({"beds": 2})
print(f"cursor output - {cursor}")

# iterate code goes here
for doc in cursor:
    print(doc)

# CLose the connection to MongoDB wher you're done
client.close()