import uuid
from dataclasses import asdict

from bson import ObjectId

from common.db import db_projects
from common.error import ServiceError, FEEDBACK_UPDATE_FAILED, FEEDBACK_NOT_FOUND, FEEDBACK_NOT_RESOLVED, PROJECT_NOT_FOUND
from model.feedback import Feedback


def feedback_submit(project_id: str, feedbacks: list[dict]) -> bool | ServiceError:
    project = db_projects.find_one({"_id": ObjectId(project_id)})
    if not project:
        return PROJECT_NOT_FOUND

    for fb in feedbacks:
        tc_id = fb["test_case_id"]
        feedback = Feedback(id=str(uuid.uuid4()), is_ok=fb["is_ok"], error_reason=fb["error_reason"], is_resolved=False)

        result = db_projects.update_one(
            {"_id": ObjectId(project_id), "test_cases.id": tc_id},
            {"$push": {"test_cases.$.feedbacks": asdict(feedback)}}
        )

        if result.modified_count == 0:
            return FEEDBACK_UPDATE_FAILED

    return True

def feedback_resolve(project_id: str, feedback_id: str) -> bool | ServiceError:
    tc_id, fb_id, feedback = _find_feedback(project_id, feedback_id)
    if not feedback:
        return FEEDBACK_NOT_FOUND

    # 문법 참고: https://www.mongodb.com/ko-kr/docs/manual/reference/operator/update/positional-filtered/#update-all-documents-that-match-arrayfilters-in-an-array
    result = db_projects.update_one(
        {"_id": ObjectId(project_id)},
        {"$set": {"test_cases.$[tc].feedbacks.$[fb].is_resolved": True}},
        array_filters=[{"tc.id": tc_id}, {"fb.id": fb_id}]
    )

    if result.modified_count == 0:
        return FEEDBACK_UPDATE_FAILED

def feedback_delete(user_id: str, feedback_id: str) -> bool | ServiceError:
    pass
