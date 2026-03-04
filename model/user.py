from dataclasses import dataclass


@dataclass
class User:
    username: str
    id: str
    password_hash: str
