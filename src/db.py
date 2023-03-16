from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
MONGO_DBNAME = os.getenv('MONGO_DBNAME')
MONGO_COLLECTION = os.getenv('MONGO_COLLECTION')


def get_db():
    client = MongoClient(MONGO_URI)
    db = client[MONGO_DBNAME]
    return db[MONGO_COLLECTION]