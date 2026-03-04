from dataclasses import asdict
from common.db import db_projects
from model.project import Project
from bson.objectid import ObjectId
from datetime import datetime


def project_create(project: Project) -> Project:
    # 모델을 그대로 저장하는 구현 예시, 실제로 여기 개발 할 때는 이 코드 지우고 만들기.
    # 참고: https://stackoverflow.com/a/62709673
    doc = asdict(project) # asdict()는 Class -> dict로 변경
    doc.pop("_id") # _id가 None으로 중복되지 않게 dict에서 제거
    result = db_projects.insert_one(doc) # MongoDB에 저장
    project._id = str(result.inserted_id) # 자동 생성된 ID를 project._id에 할당
    return project


def project_get(project_id: str) -> Project | None:
    doc = db_projects.find_one({"_id": ObjectId(project_id)})
    if not doc:
        return None
    doc["_id"] = str(doc["_id"])
    return Project(**doc) # 참고: https://stackoverflow.com/questions/3394835/use-of-args-and-kwargs


def project_list(keyword: str | None, tag: str | None) -> list[Project]:
    pass


def project_get_my(user_id: str) -> list[Project]:
    pass


def project_update(user_id: str, project_id: str, data: dict) -> bool | str:
    pass


def project_delete(user_id: str, project_id: str) -> bool | str:
    pass


def project_close(user_id: str, project_id: str) -> bool | str:
    pass


def project_add_tag(user_id: str, project_id: str, tag: str) -> bool | str:
    pass

