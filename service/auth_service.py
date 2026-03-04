from common.db import db_users
from common.error import ServiceError
from model import User


def auth_signup(username: str, user_id: str, password: str) -> User | ServiceError:
    pass


def auth_login(user_id: str, password: str) -> User | ServiceError:
    pass


def auth_get_user(user_id: str) -> User | ServiceError:
    pass
