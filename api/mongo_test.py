from pymongo import MongoClient
from collections.abc import MutableMapping

uri = "mongodb+srv://xaradxarma:fB4BCEOiUxXNZSha@cluster0.5fbfyir.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
