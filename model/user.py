from dataclasses import dataclass


@dataclass
class User:
    username: str
    login_id: str
    _id: str
    password_hash: str
