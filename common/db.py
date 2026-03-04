from pymongo import MongoClient
from pymongo.database import Database
import os

mongo_host = os.environ.get("MONGO_HOST", "localhost")
client = MongoClient(f"mongodb://{mongo_host}:27017/")


def get_db() -> Database:
    return client["jungleqa"]
