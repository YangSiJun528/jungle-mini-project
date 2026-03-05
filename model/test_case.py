from dataclasses import dataclass, field
from model.feedback import Feedback


@dataclass
class TestCase:
    id: str # 추가 시 식별을 위해서 필요함.
    content: str
    is_active: bool = True
    is_deleted: bool = False
    feedbacks: list[Feedback] = field(default_factory=list)
