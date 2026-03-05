from dataclasses import dataclass, field
from datetime import datetime

from model.tag import Tag
from model.test_case import TestCase


@dataclass
class Project:
    _id: str # ObjectId 타입으로 다루면 관리하기 까다로우므로 DB 조회 시에만 ObjectId로 변한해서 사용하기
    user_id: str # ObjectId, User의 _id 값
    title: str
    content: str
    url: str
    expired_date: datetime
    is_expired: bool
    created_at: datetime
    test_cases: list[TestCase] = field(default_factory=list)
    tags: list[Tag] = field(default_factory=list)
