from common.db import get_db
from model import User


def auth_signup(username: str, user_id: str, password: str) -> User | None:
    pass


def auth_login(user_id: str, password: str) -> User | None:
    pass


def auth_get_user(user_id: str) -> User | None:
    pass
