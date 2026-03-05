from flask import Flask, render_template, request, redirect
from model.project import Project
from model.tag import Tag
from model.test_case import TestCase
from service.project_service import project_create
from datetime import datetime

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
    return "home page"


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
    return render_template("project_form.html")


@app.route("/projects", methods=["POST"])
def create_project():
    title = request.form["title"]
    content = request.form["content"]
    url = request.form["url"]

    testcases_input = request.form.getlist("testcases[]")
    test_cases = [
        Testcase(description=tc.strip())
        for tc in testcases_input
        if tc and tc.strip()
    ]

    tags_input = request.form.get("tags", "")
    tags = [
        Tag(name=t.strip())
        for t in tags_input.split("#")
        if t.strip()
    ]

    new = Project(
        _id = None,
        titele = title,
        content = content,
        url = url,
        expired_date = datetime.now(),
        is_expired = False,
        test_cases = test_cases,
        tags = tags
    )
    
    project_create(new)

    return redirect("/")




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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
