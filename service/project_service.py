from dataclasses import asdict
from common.db import db_projects
from common.error import ServiceError, PROJECT_NOT_FOUND
from model.project import Project
from bson.objectid import ObjectId
from datetime import datetime
from flask import request
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


def project_get(project_id: str) -> Project | ServiceError:
    doc = db_projects.find_one({"_id": ObjectId(project_id)})
    if not doc:
        return PROJECT_NOT_FOUND
    doc["_id"] = str(doc["_id"])
    # 참고: https://stackoverflow.com/questions/3394835/use-of-args-and-kwargs
    return Project(**doc)


def project_list(
    page: int, keyword: str | None, tag: str | None, sort_mode: str | None = "최신"
) -> list[Project]:
    page = request.args.get("page", default=1, type=int)

    query = {}
    if keyword:
        #TODO: 키워드 기반 검색 조건 추가
        query["$or"] = [
            {"title": {"$regex": keyword, "$options": "i"}},
            {"content": {"$regex": keyword, "$options": "i"}},
        ]
    if tag:
        #TODO: 태그 기반
        query["tags"] = tag

    project_results = []
    if sort_mode:
        if sort_mode == "최신":
            #TODO: 최신 정렬 조건 추가 (created_at이 아직 정의되지 않아 없는 경우 ObjectId 기준으로 정렬될 수 있도록 유도함. ObjectId는 생성 시점이 포함되어 있어서 생성된 순서대로 정렬 가능)
            projects = db_projects.find(query).sort([("created_at", -1), ("_id", -1)]).skip((page - 1) * DISPLAY_LIMIT).limit(DISPLAY_LIMIT)
            
        if sort_mode == "임박":
            projects = db_projects.find(query).sort("expired_date", 1).skip((page - 1) * DISPLAY_LIMIT).limit(DISPLAY_LIMIT)
        
        for proj in projects:
            proj["_id"] = str(proj["_id"])
            project_results.append(Project(**proj))

    return project_results


def pagination_info(page: int) -> dict:
    tot_count = db_projects.count_documents({})
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


def project_get_my(user_id: str) -> list[Project]:
    pass


def project_update(user_id: str, project_id: str, data: dict) -> bool | ServiceError:
    pass


def project_delete(user_id: str, project_id: str) -> bool | ServiceError:
    pass


def project_close(user_id: str, project_id: str) -> bool | ServiceError:
    pass


def project_add_tag(user_id: str, project_id: str, tag: str) -> bool | ServiceError:
    pass
