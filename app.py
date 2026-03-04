from flask import Flask, render_template, request, jsonify, redirect, flash, get_flashed_messages, url_for

from common.dummy import get_user_context
from service.auth_service import auth_signup
from common.error import ServiceError
from model import project

app = Flask(__name__)
app.secret_key = "secret_key"

# 전역 컨텍스트
@app.context_processor
def inject_user_context():
    return {"user_context": get_user_context(True)}

# 도커 컴포즈 배포 시 확인용
@app.route("/health")
def health():
    return "ok"


# ------------------------
# 인증
# ------------------------

@app.route("/login", methods=["GET"])
def render_login():
    return render_template("login.html")
    
@app.route("/login", methods=["POST"])
def login():
    # 폼: user_id, password
    # 성공 -> 알잘딱
    # 실패 ->
    pass


@app.route("/signup", methods=["GET"])
def render_signup():
    return render_template("signup.html")
    # 회원가입 페이지

@app.route("/signup", methods=["POST"])
def signup():
    # 회원가입 요청
    login_id = request.form.get('login_id')
    username = request.form.get('username')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    # 비밀번호 유효성 판단
    if len(password) < 8:
        flash("비밀번호는 8글자 이상이어야 합니다")
        return redirect("/signup")
    
    elif password != confirm_password:
        flash("비밀번호가 일치하지 않습니다")
        return redirect("/signup")

    # 인증 시킨 User 객체 반환
    result = auth_signup(username, login_id, password)
    
    if isinstance(result, ServiceError):
        flash("회원가입에 실패했습니다")
        return redirect("/signup")
    
    # 회원가입 성공
    return redirect("/login")


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

@app.route("/projects/<project_id>/feedbacks", methods=["GET"])
def render_feedbacks(project_id):
    # 컨플릭 방지용으로 함수 안에서 정의
    from model.project import Project
    from service.project_service import project_get

    # 실제
    project = project_get(project_id)

    assert isinstance(project, Project) #TODO(sijun-yang): project 조회 예외 처리

    return render_template("feedback-form.html", project=project)

@app.route("/projects/<project_id>/feedbacks", methods=["POST"])
def submit_feedbacks(project_id):
    from common.error import ServiceError
    from service.feedback_service import feedback_submit

    form = request.form
    test_case_ids = [key.replace("result_", "") for key in form if key.startswith("result_")]

    feedbacks = []
    for tc_id in test_case_ids:
        is_ok = form.get(f"result_{tc_id}") == "success"
        feedbacks.append({
            "test_case_id": tc_id,
            "is_ok": is_ok,
            "error_reason": None if is_ok else form.get(f"feedback_{tc_id}"),
        })

    result = feedback_submit(project_id, feedbacks)

    if isinstance(result, ServiceError):
        # TODO(sijun-yang): 서버 에러 UI 처리
        pass

    return redirect(url_for("render_project_detail", project_id=project_id))


@app.route("/feedbacks/<feedback_id>/resolve", methods=["POST"])
def resolve_feedback(feedback_id):
    pass


@app.route("/feedbacks/<feedback_id>/delete", methods=["POST"])
def delete_feedback(feedback_id):
    # 소유자만 삭제 가능 (어뷰징 방지)
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
