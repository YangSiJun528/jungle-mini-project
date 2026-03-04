from common.db import db_projects
from model import TestCase


def testcase_add(user_id: str, project_id: str, description: str) -> TestCase | str:
    pass


def testcase_deactivate(user_id: str, testcase_id: str) -> bool | str:
    pass


def testcase_delete(user_id: str, testcase_id: str) -> bool | str:
    pass


def testcase_get_list(project_id: str, include_inactive: bool = False) -> list[TestCase]:
    pass


def testcase_is_active(testcase_id: str) -> bool:
    pass
