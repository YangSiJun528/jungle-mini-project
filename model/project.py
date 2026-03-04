from dataclasses import dataclass, field
from datetime import datetime

from model.tag import Tag
from model.test_case import TestCase


@dataclass
class Project:
    title: str
    content: str
    url: str
    expired_date: datetime
    is_expired: bool
    test_cases: list[TestCase] = field(default_factory=list)
    tags: list[Tag] = field(default_factory=list)
