from dataclasses import dataclass


@dataclass
class ServiceError:
    code: int
    message: str

# 각자 맡은 파트에서 1씩 증가시켜가면서 에러 추가하기

# 1: Auth

DUPLICATE_ID_COMMON = ServiceError(1000, "중복 ID 입니다")
NOT_EXISTS_ID_COMMON = ServiceError(1001, "해당 ID가 존재하지 않습니다")
INVALID_CREDENTIALS_COMMON = ServiceError(10012, "아이디 또는 비밀번호가 일치하지 않습니다")

# 2xxx: Project
PROJECT_COMMON = ServiceError(2000, "에러 예시")
PROJECT_NOT_FOUND = ServiceError(2001, "프로젝트를 찾을 수 없습니다.")

# 3xxx: Feedback
FEEDBACK_COMMON = ServiceError(3000, "에러 예시")
FEEDBACK_UPDATE_FAILED = ServiceError(3001, "피드백 저장에 실패했습니다.")

# 4xxx: TestCase
TESTCASE_COMMON = ServiceError(4000, "에러 예시")
