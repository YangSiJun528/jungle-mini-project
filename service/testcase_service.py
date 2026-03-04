from common.db import db_projects
from common.error import ServiceError
from model import TestCase


def testcase_add(user_id: str, project_id: str, description: str) -> TestCase | ServiceError:
    pass


def testcase_deactivate(user_id: str, testcase_id: str) -> bool | ServiceError:
    pass


def testcase_delete(user_id: str, testcase_id: str) -> bool | ServiceError:
    pass


def testcase_get_list(project_id: str, include_inactive: bool = False) -> list[TestCase]:
    pass


def testcase_is_active(testcase_id: str) -> bool:
    pass
