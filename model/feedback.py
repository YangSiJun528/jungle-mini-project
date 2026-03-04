from dataclasses import dataclass


@dataclass
class Feedback:
    is_ok: bool
    error_reason: str | None
    is_resolved: bool
