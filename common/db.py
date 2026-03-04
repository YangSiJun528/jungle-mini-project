from pymongo import MongoClient
from pymongo.collection import Collection
import os

mongo_host = os.environ.get("MONGO_HOST", "localhost")
_client = MongoClient(f"mongodb://{mongo_host}:27017/")
_db = _client["jungleqa"]

db_projects: Collection = _db["projects"]
db_users: Collection = _db["users"]
