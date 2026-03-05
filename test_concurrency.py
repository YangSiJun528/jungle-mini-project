import requests
import concurrent.futures
from datetime import datetime

# 테스트할 회원가입 주소 (포트 번호가 5001이 맞는지 확인해주세요)
TARGET_URL = "http://localhost:5001/signup"

# 동시에 보낼 가짜 유저 데이터
payload = {
    "login_id": str(datetime.now()),
    "username": "해커",
    "password": "password123!",
    "confirm_password": "password123!"
}

# 요청을 보내는 함수


def send_signup_request(thread_id):
    # 세션을 사용해서 플래시 메시지나 리다이렉트를 추적할 수도 있습니다.
    response = requests.post(TARGET_URL, data=payload)

    # 플라스크에서 성공하면 /login으로, 실패하면 /signup으로 리다이렉트 시키고 있죠?
    # 최종적으로 도착한 URL을 확인해봅니다.
    if "/login" in response.url:
        print(f"[스레드 {thread_id}] 🟢 회원가입 성공!")
    else:
        print(f"[스레드 {thread_id}] 🔴 회원가입 실패 (중복 차단됨)")


print("🔥 동시성 테스트를 시작합니다. 10개의 요청을 동시에 발사합니다!")

# 10개의 스레드를 만들어서 동시에 함수를 실행합니다.
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    # 1부터 10까지의 ID를 부여하며 동시에 실행
    futures = [executor.submit(send_signup_request, i) for i in range(1, 11)]

    # 모든 작업이 끝날 때까지 대기
    concurrent.futures.wait(futures)

print("✅ 테스트 완료!")
