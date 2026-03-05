from model import project

from common.error import ServiceError
import jwt
from common.dummy import get_user_context
from datetime import datetime
from service.auth_service import auth_signup, auth_login, create_access_token
from service.project_service import project_create
from model.test_case import TestCase
from model.tag import Tag
from model.project import Project
from flask import Flask, render_template, request, jsonify, redirect, flash, get_flashed_messages, url_for, make_response
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

app = Flask(__name__)
app.secret_key = "secret_key"

# 전역 컨텍스트


@app.errorhandler(Exception)
def global_excaption_handler(err):
    print(err)
    flash("알수없는 에러가 발생했습니다.")
    return redirect("/")


@app.errorhandler(jwt.ExpiredSignatureError)
def jwt__exception_handler(err):
    # 쿠키 지우기
    resp = make_response(redirect(url_for('render_project_list')))
    resp.delete_cookie('access_token', path='/')

    return resp


@app.context_processor
def inject_user_context():
    # print(f"유저 정보: {get_user_context(return_none=False)}")
    return {"user_context": get_user_context()}

# 도커 컴포즈 배포 시 확인용


@app.route("/health")
def health():
    return "ok"


@app.template_global()
def modify_query(**kwargs):
    args = request.args.copy()
    for key, value in kwargs.items():
        args[key] = value
    return request.path + '?' + '&'.join(f'{k}={v}' for k, v in args.items())

# ------------------------
# 인증
# ------------------------


@app.route("/login", methods=["GET"])
def render_login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    # request 받기
    login_id = request.form.get('login_id').strip()
    password = request.form.get('password')

    # 공백이 들어왔을때 에러메시지
    if not login_id or not password:
        flash("아이디/비밀번호를 입력하세요")
        return redirect("/login")

    # 로그인 인증 서비스 호출
    result = auth_login(login_id, password)

    if isinstance(result, ServiceError):
        flash(result.message)
        return redirect("/login")

    # ID,PW 유효성 검증 완료 => 토큰 생성
    jwt_token = create_access_token(result)

    resp = redirect("/")

    resp.set_cookie(
        'access_token',
        jwt_token,
        httponly=True,
        max_age=3600)

    return resp


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
        flash(result.message)
        return redirect("/signup")

    # 회원가입 성공
    return redirect("/login")


@app.route("/logout", methods=["POST"])
def logout():
    # 로그아웃 요청
    resp = make_response(redirect(url_for('render_project_list')))
    resp.delete_cookie('access_token')
    return resp


# ------------------------
# 프로젝트 조회
# ------------------------

@app.route("/", methods=["GET"])
def render_project_list():
    # 메인 페이지 - 프로젝트 목록
    from service.project_service import project_list, pagination_info
    page = request.args.get("page", default=1, type=int)
    keyword = request.args.get("keyword", default=None, type=str)
    tag = request.args.get("tag", default=None, type=str)
    sort_mode = request.args.get("sort_mode", default=None, type=str)
    projects = project_list(page=page, keyword=keyword,
                            tag=tag, sort_mode=sort_mode)
    pagination_info = pagination_info(page=page, keyword=keyword, tag=tag)

    return render_template("index.html", projects=projects, pagination_info=pagination_info)


@app.route("/projects/<project_id>", methods=["GET"])
def render_project_detail(project_id):
    from service.project_service import project_get

    project = project_get(project_id)

    for test_case in project.test_cases:
        test_case.feedbacks = sorted(
            test_case.feedbacks, key=lambda fb: fb.is_ok, reverse=True)

    if isinstance(project, ServiceError):
        flash("프로젝트를 찾을 수 없습니다. 프로젝트가 삭제되었거나 잘못된 프로젝트입니다.")
        return redirect("/")

    return render_template("project_detail.html", project=project)


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
    import uuid
    current_user = get_user_context()

    if not current_user:
        flash("프로젝트를 생성하기 위해선 로그인이 필요합니다")
        return redirect("/login")

    user_id = current_user._id
    title = request.form["title"]
    content = request.form["content"]
    url = request.form["url"]

    testcases_input = request.form.getlist("testcases[]")
    test_cases = []
    for tc in testcases_input:
        if tc and tc.strip():
            testcase = TestCase(id=str(uuid.uuid4()), content=tc.strip())
            test_cases.append(testcase)

    tags_input = request.form.get("tags", "")
    tags = []
    for t in tags_input.split("#"):
        if t.strip():
            tag = Tag(name=t.strip())
            tags.append(tag)

    new = Project(

        _id = None,
        user_id = user_id,
        title = title,
        content = content,
        url = url,
        expired_date = datetime.now(),
        created_at = datetime.now(),
        is_expired = False,
        test_cases = test_cases,
        tags = tags

    )

    project_create(new)

    return redirect("/")


@app.route("/projects/<project_id>/edit", methods=["GET"])
def render_project_edit(project_id):
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

    assert isinstance(project, Project)  # TODO(sijun-yang): project 조회 예외 처리

    return render_template("feedback-form.html", project=project)


@app.route("/projects/<project_id>/feedbacks", methods=["POST"])
def submit_feedbacks(project_id):
    from common.error import ServiceError
    from service.feedback_service import feedback_submit

    form = request.form
    test_case_ids = [key.replace("result_", "")
                     for key in form if key.startswith("result_")]

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
