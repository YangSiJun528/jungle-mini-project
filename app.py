from flask import Flask

app = Flask(__name__)

# 도커 컴포즈 배포 시 확인용
@app.route("/health")
def health():
    return "ok"


# ------------------------
# 인증
# ------------------------

@app.route("/login", methods=["GET"])
def render_login():
    # 로그인 페이지
    pass


@app.route("/login", methods=["POST"])
def login():
    # 폼: user_id, password
    # 성공 -> 알잘딱
    # 실패 ->
    pass


@app.route("/signup", methods=["GET"])
def render_signup():
    # 회원가입 페이지
    pass


@app.route("/signup", methods=["POST"])
def signup():
    # 회원가입 요청
    pass


@app.route("/logout", methods=["POST"])
def logout():
    # 로그아웃 요청
    pass


# ------------------------
# 프로젝트 조회
# ------------------------

@app.route("/", methods=["GET"])
def render_project_list():
    # 메인 페이지 - 프로젝트 목록
    # 쿼리 파라미터 처리 필요
    pass


@app.route("/projects/<project_id>", methods=["GET"])
def render_project_detail(project_id):
    # 프로젝트 상세 페이지 - 테스트케이스 + 피드백 포함
    pass


@app.route("/my-projects", methods=["GET"])
def render_my_projects():
    # 내 프로젝트 목록
    pass

# ------------------------
# 프로젝트 생성, 수정, 삭제
# ------------------------

@app.route("/projects/new", methods=["GET"])
def render_project_form():
    # 프로젝트 생성 폼 페이지
    pass


@app.route("/projects/new", methods=["POST"])
def create_project():
    pass


@app.route("/projects/<project_id>/edit", methods=["GET"])
def render_project_edit(project_id):
    # 프로젝트 수정 폼 (소유자만 가능)
    pass


@app.route("/projects/<project_id>/edit", methods=["POST"])
def update_project(project_id):
    # 소유자 확인 필요
    pass


@app.route("/projects/<project_id>/delete", methods=["POST"])
def delete_project(project_id):
    pass


@app.route("/projects/<project_id>/close", methods=["POST"])
def close_project(project_id):
    pass


# ------------------------
# 태그
# ------------------------

@app.route("/tags/<tag_name>", methods=["GET"])
def render_tag_search(tag_name):
    # 태그 검색 결과 페이지
    pass

# ------------------------
# 테스트케이스
# ------------------------

@app.route("/projects/<project_id>/testcases", methods=["POST"])
def add_testcase(project_id):
    pass


@app.route("/testcases/<testcase_id>/deactivate", methods=["POST"])
def deactivate_testcase(testcase_id):
    pass


@app.route("/testcases/<testcase_id>/delete", methods=["POST"])
def delete_testcase(testcase_id):
    pass


# ------------------------
# 피드백
# ------------------------

@app.route("/projects/<project_id>/feedbacks", methods=["POST"])
def submit_feedbacks(project_id):
    pass


@app.route("/feedbacks/<feedback_id>/resolve", methods=["POST"])
def resolve_feedback(feedback_id):
    pass


@app.route("/feedbacks/<feedback_id>/delete", methods=["POST"])
def delete_feedback(feedback_id):
    # 소유자만 삭제 가능 (어뷰징 방지)
    pass

def test_db():
    from dataclasses import asdict
    from datetime import datetime
    from common.db import db_projects
    from model.project import Project
    from service.project_service import project_create, project_get

    db_projects.drop() # 초기화

    p = Project(
        _id="",
        title="테스트 프로젝트 이름",
        content="테스트 내용입니다 테스트 내용입니다 테스트 내용입니다 테스트 내용입니다 테스트 내용입니다 테스트 내용입니다 테스트 내용입니다",
        url="https://google.com",
        expired_date=datetime(2026, 12, 31),
        is_expired=False,
    )
    created = project_create(p)
    print("=== 생성 결과 ===")
    print(asdict(created))

    found = project_get(created._id)
    print("=== 조회 결과 ===")
    print(asdict(found))

    not_found = project_get("000000000000000000000000")
    print("=== 없는 프로젝트 조회 ===")
    print(not_found)

    db_projects.drop()

if __name__ == "__main__":
    test_db()
    #app.run(host="0.0.0.0", port=5001)
