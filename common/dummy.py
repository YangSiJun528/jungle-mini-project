from model.user import User
import jwt
from flask import request, flash, make_response, redirect, url_for

# 현재 인증 된 사용자 정보를 불려오는 역할인데, 개발 도중에는 더미로 사용. 인증 파트 팀원이 구현하기
# 로그인이 안된 상태면 None을 반환하고, 아니면 더미 User 객체를 반환. 바꿔가면서 UI 테스트 ㄱㄱ

SECRET_KEY = "jungle_mini_project2131236532dsafxd24weqsadasd"


def get_user_context() -> User | None:

    token = request.cookies.get('access_token')

    if not token:
        return None

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])

        user_id = payload.get('user_id')
        login_id = payload.get('login_id')
        username = payload.get('username')

        return User(
            _id=user_id,
            username=username,
            login_id=login_id,
            password_hash="",
        )

    except jwt.ExpiredSignatureError:
        flash("로그인 시간이 만료되었습니다. 다시 로그인 해주세요.", "danger")
        return None
