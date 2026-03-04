from dataclasses import dataclass


@dataclass
class User:
    username: str
    _id: str
    password_hash: str
