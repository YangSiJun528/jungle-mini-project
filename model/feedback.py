from dataclasses import dataclass


@dataclass
class Feedback:
    id: str
    is_ok: bool
    error_reason: str | None
    is_resolved: bool
