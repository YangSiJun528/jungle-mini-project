from common.db import db_projects
from model import Feedback


def feedback_submit(project_id: str, feedbacks: list[dict]) -> dict | str:
    pass


def feedback_resolve(user_id: str, feedback_id: str) -> bool | str:
    pass


def feedback_delete(user_id: str, feedback_id: str) -> bool | str:
    pass


def feedback_get_list(testcase_id: str, include_resolved: bool = False) -> list[Feedback]:
    pass
