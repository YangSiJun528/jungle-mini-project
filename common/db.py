from pymongo import MongoClient
from pymongo.collection import Collection
import os

mongo_host = os.environ.get("MONGO_HOST", "localhost")

# _를 붙여서 "db.이상한이름" 에 접근하는거 예방
_client = MongoClient(f"mongodb://{mongo_host}:27017/")
_db = _client["jungleqa"]

# DB 접근 시 이걸로 고정해서 처리
db_projects: Collection = _db["projects"]
db_users: Collection = _db["users"]

# 시작 될때, DB 측에서 login_id에 유니크를 걸어서 중복 id를 방지
db_users.create_index("login_id", unique=True)
