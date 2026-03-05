from common.db import db_users
from common.error import ServiceError
from common import error
from model import User
import bcrypt
import jwt


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

    # login_id로 유저 조회
    # 있으면 bcrypt로 비밀번호 검증
    id_exists = db_users.find_one({"login_id": user_id})

    if not id_exists:
        return error.NOT_EXISTS_ID_COMMON

    hashed_password = id_exists['password_hash']
    byted_hashed_password = hashed_password.encode('utf-8')

    is_password_match = bcrypt.checkpw(password.encode("utf-8"),
                                       byted_hashed_password)
    # 비밀번호가 일치하지 않으면 에러메시지
    if not is_password_match:
        return error.INVALID_CREDENTIALS_COMMON
    # User 정보 반환 (password는 X)
    return User(username=id_exists["username"],
                login_id=id_exists["login_id"],
                _id=str(id_exists["_id"]))

def create_access_token(user: User) -> str:
    # 1) payload 만들기 (user_id, login_id, exp)
    # 2) jwt.encode로 토큰 생성
    return token

def auth_get_user(user_id: str) -> User | ServiceError:
    return ServiceError