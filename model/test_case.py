from dataclasses import dataclass, field
from model.feedback import Feedback


@dataclass
class TestCase:
    id: str # 추가 시 식별을 위해서 필요함.
    content: str
    is_active: bool = True
    feedbacks: list[Feedback] = field(default_factory=list)
