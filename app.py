from flask import (
    Flask,
    render_template,
    request,
    redirect,
    flash,
    url_for,
    make_response,
)
from dotenv import load_dotenv
import jwt
from datetime import datetime

from common.dummy import get_user_context
from common.error import ServiceError
from model.project import Project
from model.tag import Tag
from model.test_case import TestCase
from service.auth_service import auth_signup, auth_login, create_access_token
from service.project_service import (
    project_create,
    project_get,
    project_update,
)

load_dotenv()

app = Flask(__name__)
app.secret_key = "secret_key"


# ------------------------
# 전역 에러 처리
# ------------------------
@app.errorhandler(Exception)
def global_excaption_handler(err):
    # 원인 확인용
    print(err)
    flash("알수없는 에러가 발생했습니다.")
    return redirect("/")


@app.errorhandler(jwt.ExpiredSignatureError)
def jwt__exception_handler(err):
    # 쿠키 지우기
    resp = make_response(redirect(url_for("render_project_list")))
    resp.delete_cookie("access_token", path="/")
    return resp


@app.context_processor
def inject_user_context():
    return {"user_context": get_user_context()}


@app.template_global()
def modify_query(**kwargs):
    args = request.args.copy()
    for key, value in kwargs.items():
        args[key] = value
    return request.path + "?" + "&".join(f"{k}={v}" for k, v in args.items())


# ------------------------
# 헬스체크
# ------------------------
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
    login_id = (request.form.get("login_id") or "").strip()
    password = request.form.get("password") or ""

    if not login_id or not password:
        flash("아이디/비밀번호를 입력하세요")
        return redirect("/login")

    result = auth_login(login_id, password)
    if isinstance(result, ServiceError):
        flash(result.message)
        return redirect("/login")

    jwt_token = create_access_token(result)

    resp = make_response(redirect("/"))
    resp.set_cookie(
        "access_token",
        jwt_token,
        httponly=True,
        max_age=3600,
    )
    return resp


@app.route("/signup", methods=["GET"])
def render_signup():
    return render_template("signup.html")


@app.route("/signup", methods=["POST"])
def signup():
    login_id = (request.form.get("login_id") or "").strip()
    username = (request.form.get("username") or "").strip()
    password = request.form.get("password") or ""
    confirm_password = request.form.get("confirm_password") or ""

    if len(password) < 8:
        flash("비밀번호는 8글자 이상이어야 합니다")
        return redirect("/signup")

    if password != confirm_password:
        flash("비밀번호가 일치하지 않습니다")
        return redirect("/signup")

    result = auth_signup(username, login_id, password)
    if isinstance(result, ServiceError):
        flash(result.message)
        return redirect("/signup")

    return redirect("/login")


@app.route("/logout", methods=["POST"])
def logout():
    resp = make_response(redirect(url_for("render_project_list")))
    resp.delete_cookie("access_token")
    return resp


# ------------------------
# 프로젝트 조회
# ------------------------
@app.route("/", methods=["GET"])
def render_project_list():
    from service.project_service import project_list, pagination_info

    page = request.args.get("page", default=1, type=int)
    keyword = request.args.get("keyword", default=None, type=str)
    tag = request.args.get("tag", default=None, type=str)
    sort_mode = request.args.get("sort_mode", default=None, type=str)

    projects = project_list(page=page, keyword=keyword, tag=tag, sort_mode=sort_mode)
    page_info = pagination_info(page=page, keyword=keyword, tag=tag)

    return render_template("index.html", projects=projects, pagination_info=page_info)


@app.route("/projects/<project_id>", methods=["GET"])
def render_project_detail(project_id):
    proj = project_get(project_id)
    if isinstance(proj, ServiceError):
        flash("프로젝트를 찾을 수 없습니다. 프로젝트가 삭제되었거나 잘못된 프로젝트입니다.")
        return redirect("/")

    # 피드백 정렬 (성공/실패 등 기준)
    for test_case in proj.test_cases:
        test_case.feedbacks = sorted(test_case.feedbacks, key=lambda fb: fb.is_ok, reverse=True)

    return render_template("project_detail.html", project=proj)


@app.route("/my-projects", methods=["GET"])
def render_my_projects():
    # 내 프로젝트 목록
    current_user = get_user_context()

    if not current_user:
        flash("내 프로젝트를 보려면 로그인이 필요합니다.")
        return redirect("/login")

    current_user_id = current_user._id
    keyword = request.args.get("keyword", default=None, type=str)
    tag = request.args.get("tag", default=None, type=str)
    sort_mode = request.args.get("sort_mode", default=None, type=str)
    from service.project_service import project_get_my
    projects = project_get_my(user_id=current_user_id, keyword=keyword, tag=tag, sort_mode=sort_mode)

    return render_template("my-projects.html", projects=projects)


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

    title = (request.form.get("title") or "").strip()
    content = (request.form.get("content") or "").strip()
    url = (request.form.get("url") or "").strip()

    expired_date_str = (request.form.get("expired_date") or "").strip()
    if not title or not content or not url or not expired_date_str:
        flash("필수 항목을 모두 입력하세요")
        return redirect("/projects/new")

    expired_date = datetime.strptime(expired_date_str, "%Y-%m-%d")

    testcases_input = request.form.getlist("testcases[]")
    test_cases = []
    for tc in testcases_input:
        tc = (tc or "").strip()
        if tc:
            test_cases.append(TestCase(id=str(uuid.uuid4()), content=tc))

    tags_input = request.form.get("tags", "") or ""
    tags = []
    for t in tags_input.split("#"):
        t = t.strip()
        if t:
            tags.append(Tag(name=t))

    new_project = Project(
        _id=None,
        user_id=user_id,
        title=title,
        content=content,
        url=url,
        expired_date=expired_date,
        created_at=datetime.now(),
        is_expired=False,
        test_cases=test_cases,
        tags=tags,
    )

    project_create(new_project)
    return redirect("/")


@app.route("/projects/<project_id>/edit", methods=["GET"])
def render_project_edit(project_id):
    current_user = get_user_context()
    if not current_user:
        flash("로그인이 필요합니다")
        return redirect("/login")

    user_id = current_user._id

    project_or_err = project_get(project_id)
    if isinstance(project_or_err, ServiceError):
        flash("프로젝트를 가져오는데 실패했습니다")
        return redirect("/")

    proj = project_or_err

    if proj.user_id != user_id:
        flash("프로젝트를 수정하기 위해선 본인이 작성한 프로젝트여야합니다")
        return redirect("/")

    # 등록 폼을 수정 폼으로 재사용
    return render_template("project_form.html", project=proj)


@app.route("/projects/<project_id>/edit", methods=["POST"])
def update_project(project_id):
    current_user = get_user_context()
    if not current_user:
        flash("로그인이 필요합니다")
        return redirect("/login")

    user_id = current_user._id

    title = (request.form.get("title") or "").strip()
    content = (request.form.get("content") or "").strip()
    url = (request.form.get("url") or "").strip()
    expired_date_str = (request.form.get("expired_date") or "").strip()

    if not title or not content or not url or not expired_date_str:
        flash("필수 항목을 모두 입력하세요")
        return redirect(f"/projects/{project_id}/edit")

    expired_date = datetime.strptime(expired_date_str, "%Y-%m-%d")

    # B안: 태그 통째로 덮어쓰기
    tags_input = request.form.get("tags", "") or ""
    tags = []
    for t in tags_input.split("#"):
        t = t.strip()
        if t:
            tags.append({"name": t})

    data = {
        "title": title,
        "content": content,
        "url": url,
        "expired_date": expired_date,
        "tags": tags,
    }

    ok_or_err = project_update(user_id, project_id, data)
    if isinstance(ok_or_err, ServiceError):
        flash("수정 반영 중 오류 발생")
        return redirect("/")

    return redirect(f"/projects/{project_id}")


@app.route("/projects/<project_id>/delete", methods=["POST"])
def delete_project(project_id):
    # TODO
    return "TODO"


@app.route("/projects/<project_id>/close", methods=["POST"])
def close_project(project_id):
    # TODO
    return "TODO"


# ------------------------
# 태그
# ------------------------
@app.route("/tags/<tag_name>", methods=["GET"])
def render_tag_search(tag_name):
    # TODO
    return "TODO"


# ------------------------
# 테스트케이스
# ------------------------
@app.route("/projects/<project_id>/testcases", methods=["POST"])
def add_testcase(project_id):
    # TODO
    return "TODO"


@app.route("/testcases/<testcase_id>/deactivate", methods=["POST"])
def deactivate_testcase(testcase_id):
    # TODO
    return "TODO"


@app.route("/testcases/<testcase_id>/delete", methods=["POST"])
def delete_testcase(testcase_id):
    # TODO
    return "TODO"


# ------------------------
# 피드백
# ------------------------
@app.route("/projects/<project_id>/feedbacks", methods=["GET"])
def render_feedbacks(project_id):
    from model.project import Project as ProjectModel

    proj = project_get(project_id)
    if isinstance(proj, ServiceError):
        flash("프로젝트를 찾을 수 없습니다.")
        return redirect("/")

    assert isinstance(proj, ProjectModel)
    return render_template("feedback-form.html", project=proj)


@app.route("/projects/<project_id>/feedbacks", methods=["POST"])
def submit_feedbacks(project_id):
    from service.feedback_service import feedback_submit

    form = request.form
    test_case_ids = [key.replace("result_", "") for key in form if key.startswith("result_")]

    feedbacks = []
    for tc_id in test_case_ids:
        is_ok = form.get(f"result_{tc_id}") == "success"
        feedbacks.append(
            {
                "test_case_id": tc_id,
                "is_ok": is_ok,
                "error_reason": None if is_ok else form.get(f"feedback_{tc_id}"),
            }
        )

    result = feedback_submit(project_id, feedbacks)
    if isinstance(result, ServiceError):
        # TODO: 서버 에러 UI 처리
        flash("피드백 제출 중 오류가 발생했습니다.")
        return redirect(url_for("render_project_detail", project_id=project_id))

    return redirect(url_for("render_project_detail", project_id=project_id))


@app.route("/feedbacks/<feedback_id>/resolve", methods=["POST"])
def resolve_feedback(feedback_id):
    # TODO
    return "TODO"


@app.route("/feedbacks/<feedback_id>/delete", methods=["POST"])
def delete_feedback(feedback_id):
    # TODO
    return "TODO"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)