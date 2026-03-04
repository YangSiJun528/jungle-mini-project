from dataclasses import asdict

from bson import ObjectId

from common.db import db_projects
from common.error import ServiceError, FEEDBACK_UPDATE_FAILED, PROJECT_NOT_FOUND
from model.feedback import Feedback


def feedback_submit(project_id: str, feedbacks: list[dict]) -> bool | ServiceError:
    project = db_projects.find_one({"_id": ObjectId(project_id)})
    if not project:
        return PROJECT_NOT_FOUND

    for fb in feedbacks:
        tc_id = fb["test_case_id"]
        feedback = Feedback(is_ok=fb["is_ok"], error_reason=fb["error_reason"])

        result = db_projects.update_one(
            {"_id": ObjectId(project_id), "test_cases.id": tc_id},
            {"$push": {"test_cases.$.feedbacks": asdict(feedback)}}
        )

        if result.modified_count == 0:
            return FEEDBACK_UPDATE_FAILED

    return True


def feedback_resolve(user_id: str, feedback_id: str) -> bool | ServiceError:
    pass


def feedback_delete(user_id: str, feedback_id: str) -> bool | ServiceError:
    pass


def feedback_get_list(testcase_id: str, include_resolved: bool = False) -> list[Feedback]:
    pass
