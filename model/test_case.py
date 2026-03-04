from dataclasses import dataclass, field
from model.feedback import Feedback


@dataclass
class TestCase:
    content: str
    feedbacks: list[Feedback] = field(default_factory=list)
