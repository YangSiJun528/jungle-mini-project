from model.user import User

"""현재 인증 된 사용자 정보를 불려오는 역할인데, 개발 도중에는 더미로 사용. 인증 파트 팀원이 구현 ㄱㄱ"""
def get_user_context(return_none: bool = False) -> User | None:
    if return_none:
        return None

    return User(
        _id="000000000000000000000000",
        username="더미유저",
        password_hash="no_password",
    )
