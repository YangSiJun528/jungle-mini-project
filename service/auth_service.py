from common.db import db_users
from common.error import ServiceError
from common import error
from model import User
import bcrypt


def auth_signup(username: str, user_id: str, password: str) -> User | ServiceError:
    # 1. 아이디 중복 체크
    existing_user = db_users.find_one({"login_id": user_id})
    if existing_user:
        return error.DUPLICATE_ID_COMMON
    
    # 2. 비밀번호 암호화
    byted_password = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(byted_password, bcrypt.gensalt())
    hashed_password_str = hashed_password.decode('utf-8')

    # 3. DB 저장   
    result = db_users.insert_one({
        "username": username,
        "login_id": user_id,
        "password_hash": hashed_password_str
    })

    # 4. User 반환
    return User(
        username=username,
        login_id=user_id,
        password_hash=hashed_password_str,
        _id=str(result.inserted_id))

def auth_login(user_id: str, password: str) -> User | ServiceError:
    pass


def auth_get_user(user_id: str) -> User | ServiceError:
    pass
