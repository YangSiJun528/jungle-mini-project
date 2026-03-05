from dataclasses import dataclass, field
from datetime import datetime

from model.tag import Tag
from model.test_case import TestCase


@dataclass
class Project:
    _id: str # ObjectId 타입으로 다루면 관리하기 까다로우므로 DB 조회 시에만 ObjectId로 변한해서 사용하기
    title: str
    content: str
    url: str
    expired_date: datetime
    is_expired: bool
    created_at: datetime = field(default_factory=datetime.now) # TODO: 연동 끝나고 마지막에 직접 값 할당하게 하기
    test_cases: list[TestCase] = field(default_factory=list)
    tags: list[Tag] = field(default_factory=list)
