from dataclasses import asdict
from common.db import db_projects
from common.error import ServiceError, PROJECT_NOT_FOUND, PROJECT_DELETE_FAILED
from model.project import Project
from model.test_case import TestCase
from model.feedback import Feedback
from model.tag import Tag
from bson.objectid import ObjectId
from datetime import datetime
import math

DISPLAY_LIMIT = 8


def project_create(project: Project) -> Project:
    # 모델을 그대로 저장하는 구현 예시, 실제로 여기 개발 할 때는 이 코드 지우고 만들기.
    # 참고: https://stackoverflow.com/a/62709673
    doc = asdict(project)  # asdict()는 Class -> dict로 변경
    doc.pop("_id")  # _id가 None으로 중복되지 않게 dict에서 제거
    result = db_projects.insert_one(doc)  # MongoDB에 저장
    project._id = str(result.inserted_id)  # 자동 생성된 ID를 project._id에 할당
    return project

def project_update(user_id: str, project_id: str, data:dict) -> None:
    allowed = {"title", "content", "url", "expired_date", "tags"}
    update_data = {k: v for k, v in data.items() if k in allowed}

    result = db_projects.update_one(
        {"_id": ObjectId(project_id), "user_id": user_id},
        {"$set": update_data},
    )

def project_get(project_id: str) -> Project | ServiceError:
    doc = db_projects.find_one({"_id": ObjectId(project_id)})
    if not doc:
        return PROJECT_NOT_FOUND
    doc["_id"] = str(doc["_id"])

    test_cases = []
    raw_test_cases = doc.get("test_cases", [])

    for tc in raw_test_cases:
        feedbacks = []
        raw_feedbacks = tc.get("feedbacks", [])

        for fb in raw_feedbacks:
            feedback = Feedback(**fb)
            feedbacks.append(feedback)

        tc_dict = dict(tc)
        tc_dict["feedbacks"] = feedbacks # feedbacks이 dict 상태인데, 이걸 변경한 Feedback 객체로 변경

        test_case = TestCase(**tc_dict)
        test_cases.append(test_case)

    doc["test_cases"] = test_cases

    tags = []
    raw_tags = doc.get("tags", [])

    for t in raw_tags:
        tag = Tag(**t)
        tags.append(tag)

    doc["tags"] = tags

    return Project(**doc)  # 참고: https://stackoverflow.com/questions/3394835/use-of-args-and-kwargs


def project_list(
        keyword: str | None, tag: str | None, sort_mode: str | None, page: int = 1,
) -> list[Project]:
    from pymongo import DESCENDING, ASCENDING
    size = 8
    sort_options = {
        "latest": [("created_at", DESCENDING)],
        "deadline": [("expired_date", ASCENDING), ("created_at", DESCENDING)],
    }

    sort_params = "latest"
    if sort_mode is not None:
        sort_params = sort_mode

    conditions = []
    if keyword:
        conditions.append({
            "$or": [
                {"title": {"$regex": keyword, "$options": "i"}},
                {"content": {"$regex": keyword, "$options": "i"}},
            ]
        })
    if tag:
        conditions.append({"tags": {"$elemMatch": {"name": tag}}})
    query = {"$and": conditions} if conditions else {}

    assert sort_options[sort_params] is not None
    sort = sort_options[sort_params]

    project_results = db_projects.find(query).sort(sort).skip((page - 1) * size).limit(size)

    return project_results


def pagination_info(keyword: str | None, tag: str | None, page: int = 1) -> dict:
    conditions = []
    if keyword:
        conditions.append({
            "$or": [
                {"title": {"$regex": keyword, "$options": "i"}},
                {"content": {"$regex": keyword, "$options": "i"}},
            ]
        })
    if tag:
        conditions.append({"tags": {"$elemMatch": {"name": tag}}})

    tot_count = db_projects.count_documents({"$and": conditions} if conditions else {})
    last_page_num = math.ceil(tot_count / DISPLAY_LIMIT)

    # 블록: 페이지 표시 단위를 의미
    BLOCK_SIZE = 5
    # 첫번째 블록의 block_num = 0
    block_num = int((page - 1) / BLOCK_SIZE)
    block_start = block_num * BLOCK_SIZE + 1
    block_end = block_start + BLOCK_SIZE - 1
    return {
        "page": page,
        "block_start": block_start,
        "block_end": block_end,
        "last_page_num": last_page_num,
    }


def project_get_my(user_id: str, keyword: str | None, tag: str | None, sort_mode: str | None) -> list[Project]:
    from pymongo import DESCENDING, ASCENDING
    sort_options = {
        "latest": [("created_at", DESCENDING)],
        "deadline": [("expired_date", ASCENDING), ("created_at", DESCENDING)],
    }

    sort_params = "latest"
    if sort_mode is not None:
        sort_params = sort_mode

    conditions = [ {"user_id": user_id} ]
    if keyword:
        conditions.append({
            "$or": [
                {"title": {"$regex": keyword, "$options": "i"}},
                {"content": {"$regex": keyword, "$options": "i"}},
            ]
        })
    if tag:
        conditions.append({"tags": {"$elemMatch": {"name": tag}}})
    query = {"$and": conditions} if conditions else {}

    assert sort_options[sort_params] is not None
    sort = sort_options[sort_params]

    project_results = db_projects.find(query).sort(sort)
    return project_results


def project_delete(user_id: str, project_id: str) -> bool | ServiceError:
    result = db_projects.delete_one({"_id": ObjectId(project_id), "user_id": user_id})
    if result.deleted_count == 0:
        return PROJECT_DELETE_FAILED
    return True


def project_close(user_id: str, project_id: str) -> bool | ServiceError:
    pass


def project_add_tag(user_id: str, project_id: str, tag: str) -> bool | ServiceError:
    pass
