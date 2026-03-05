도커로 프로젝트 실행, 이미 열려있으면 종료해도 됨.

```
docker compose up --build
```

```
docker compose exec mongo mongosh
```


```
use jungleqa
```

아래 drop으로 기존 mongodb 데이터가 제거되므로 주의

```
db.projects.drop()
```

```
db.projects.insertMany([
  {
    title: "배달의민족",
    content: "배달의민족 서비스의 QA 테스트 프로젝트입니다. 주요 기능에 대한 피드백을 수집합니다.",
    url: "https://example.com/baemin",
    expired_date: new Date("2026-06-01"),
    is_expired: false,
    created_at: new Date("2026-01-10"),
    test_cases: [
      { id: crypto.randomUUID(), content: "로그인이 정상적으로 동작해야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }, { id: crypto.randomUUID(), is_ok: false, error_reason: "버튼 클릭 시 반응이 없음", is_resolved: false }] },
      { id: crypto.randomUUID(), content: "주문 기능이 정상적으로 동작해야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: true }] },
      { id: crypto.randomUUID(), content: "결제 프로세스가 정상적으로 완료되어야 한다.", feedbacks: [] },
      { id: crypto.randomUUID(), content: "검색 기능이 정상적으로 동작해야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: false, error_reason: "페이지가 무한 로딩됨", is_resolved: false }] },
    ],
    tags: [{ name: "웹" }, { name: "모바일" }]
  },
  {
    title: "당근마켓",
    content: "당근마켓 서비스의 QA 테스트 프로젝트입니다. 주요 기능에 대한 피드백을 수집합니다.",
    url: "https://example.com/daangn",
    expired_date: new Date("2026-07-15"),
    is_expired: false,
    created_at: new Date("2026-01-15"),
    test_cases: [
      { id: crypto.randomUUID(), content: "회원가입 시 유효성 검사가 동작해야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: true }, { id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }] },
      { id: crypto.randomUUID(), content: "게시글 작성이 정상적으로 동작해야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: false, error_reason: "500 에러 발생", is_resolved: false }] },
      { id: crypto.randomUUID(), content: "이미지 업로드가 정상적으로 동작해야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: false, error_reason: "타임아웃 에러 발생", is_resolved: false }, { id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }] },
      { id: crypto.randomUUID(), content: "채팅 기능이 정상적으로 동작해야 한다.", feedbacks: [] },
      { id: crypto.randomUUID(), content: "좋아요 기능이 정상적으로 동작해야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }] },
    ],
    tags: [{ name: "모바일" }, { name: "프론트엔드" }]
  },
  {
    title: "토스",
    content: "토스 서비스의 QA 테스트 프로젝트입니다. 주요 기능에 대한 피드백을 수집합니다.",
    url: "https://example.com/toss",
    expired_date: new Date("2026-05-20"),
    is_expired: false,
    created_at: new Date("2026-01-22"),
    test_cases: [
      { id: crypto.randomUUID(), content: "로그인이 정상적으로 동작해야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }] },
      { id: crypto.randomUUID(), content: "송금 기능이 정상적으로 동작해야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }, { id: crypto.randomUUID(), is_ok: false, error_reason: "잘못된 데이터가 표시됨", is_resolved: false }] },
      { id: crypto.randomUUID(), content: "알림 설정이 정상적으로 저장되어야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: false, error_reason: "UI가 깨져서 표시됨", is_resolved: false }] },
    ],
    tags: [{ name: "모바일" }, { name: "백엔드" }, { name: "API" }]
  },
  {
    title: "카카오톡",
    content: "카카오톡 서비스의 QA 테스트 프로젝트입니다. 주요 기능에 대한 피드백을 수집합니다.",
    url: "https://example.com/kakaotalk",
    expired_date: new Date("2026-08-30"),
    is_expired: false,
    created_at: new Date("2026-02-01"),
    test_cases: [
      { id: crypto.randomUUID(), content: "메시지 전송이 정상적으로 동작해야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: true }, { id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }] },
      { id: crypto.randomUUID(), content: "프로필 수정이 정상적으로 반영되어야 한다.", feedbacks: [] },
      { id: crypto.randomUUID(), content: "공유 기능이 정상적으로 동작해야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: false, error_reason: "권한 없음 에러 표시됨", is_resolved: false }] },
      { id: crypto.randomUUID(), content: "검색 기능이 정상적으로 동작해야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }] },
      { id: crypto.randomUUID(), content: "다크모드 전환이 정상적으로 동작해야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }, { id: crypto.randomUUID(), is_ok: false, error_reason: "UI가 깨져서 표시됨", is_resolved: false }] },
      { id: crypto.randomUUID(), content: "알림 설정이 정상적으로 저장되어야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }] },
    ],
    tags: [{ name: "모바일" }, { name: "UI" }]
  },
  {
    title: "네이버지도",
    content: "네이버지도 서비스의 QA 테스트 프로젝트입니다. 주요 기능에 대한 피드백을 수집합니다.",
    url: "https://example.com/navermap",
    expired_date: new Date("2026-09-10"),
    is_expired: false,
    created_at: new Date("2026-02-05"),
    test_cases: [
      { id: crypto.randomUUID(), content: "지도 로딩이 정상적으로 동작해야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }] },
      { id: crypto.randomUUID(), content: "길찾기 기능이 정상적으로 동작해야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: false, error_reason: "페이지가 무한 로딩됨", is_resolved: false }, { id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }] },
      { id: crypto.randomUUID(), content: "검색 기능이 정상적으로 동작해야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }, { id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }] },
      { id: crypto.randomUUID(), content: "즐겨찾기 저장이 정상적으로 동작해야 한다.", feedbacks: [] },
    ],
    tags: [{ name: "웹" }, { name: "모바일" }, { name: "API" }]
  },
  {
    title: "쿠팡",
    content: "쿠팡 서비스의 QA 테스트 프로젝트입니다. 주요 기능에 대한 피드백을 수집합니다.",
    url: "https://example.com/coupang",
    expired_date: new Date("2026-04-15"),
    is_expired: false,
    created_at: new Date("2026-02-10"),
    test_cases: [
      { id: crypto.randomUUID(), content: "장바구니 추가가 정상적으로 동작해야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }, { id: crypto.randomUUID(), is_ok: false, error_reason: "버튼 클릭 시 반응이 없음", is_resolved: false }] },
      { id: crypto.randomUUID(), content: "결제 프로세스가 정상적으로 완료되어야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: false, error_reason: "500 에러 발생", is_resolved: false }] },
      { id: crypto.randomUUID(), content: "상세 페이지에서 정보가 올바르게 표시되어야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }] },
      { id: crypto.randomUUID(), content: "로그인이 정상적으로 동작해야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: true }, { id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }] },
      { id: crypto.randomUUID(), content: "검색 기능이 정상적으로 동작해야 한다.", feedbacks: [] },
      { id: crypto.randomUUID(), content: "로그아웃이 정상적으로 동작해야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }] },
      { id: crypto.randomUUID(), content: "댓글 작성이 정상적으로 동작해야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: false, error_reason: "권한 없음 에러 표시됨", is_resolved: false }, { id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }] },
    ],
    tags: [{ name: "웹" }, { name: "백엔드" }]
  },
  {
    title: "야놀자",
    content: "야놀자 서비스의 QA 테스트 프로젝트입니다. 주요 기능에 대한 피드백을 수집합니다.",
    url: "https://example.com/yanolja",
    expired_date: new Date("2026-10-01"),
    is_expired: false,
    created_at: new Date("2026-02-18"),
    test_cases: [
      { id: crypto.randomUUID(), content: "예약 기능이 정상적으로 동작해야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }] },
      { id: crypto.randomUUID(), content: "결제 프로세스가 정상적으로 완료되어야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }, { id: crypto.randomUUID(), is_ok: false, error_reason: "타임아웃 에러 발생", is_resolved: false }] },
      { id: crypto.randomUUID(), content: "메인 페이지가 정상적으로 로딩되어야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }] },
    ],
    tags: [{ name: "웹" }, { name: "QA" }]
  },
  {
    title: "직방",
    content: "직방 서비스의 QA 테스트 프로젝트입니다. 주요 기능에 대한 피드백을 수집합니다.",
    url: "https://example.com/zigbang",
    expired_date: new Date("2026-06-20"),
    is_expired: false,
    created_at: new Date("2026-02-25"),
    test_cases: [
      { id: crypto.randomUUID(), content: "지도 기반 검색이 정상적으로 동작해야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: false, error_reason: "잘못된 데이터가 표시됨", is_resolved: false }] },
      { id: crypto.randomUUID(), content: "매물 상세 페이지가 올바르게 표시되어야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }, { id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }] },
      { id: crypto.randomUUID(), content: "로그인이 정상적으로 동작해야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }] },
      { id: crypto.randomUUID(), content: "프로필 수정이 정상적으로 반영되어야 한다.", feedbacks: [] },
      { id: crypto.randomUUID(), content: "이미지 업로드가 정상적으로 동작해야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: false, error_reason: "UI가 깨져서 표시됨", is_resolved: false }, { id: crypto.randomUUID(), is_ok: false, error_reason: "500 에러 발생", is_resolved: false }] },
    ],
    tags: [{ name: "웹" }, { name: "프론트엔드" }, { name: "API" }]
  },
  {
    title: "번개장터",
    content: "번개장터 서비스의 QA 테스트 프로젝트입니다. 주요 기능에 대한 피드백을 수집합니다.",
    url: "https://example.com/bunjang",
    expired_date: new Date("2026-07-01"),
    is_expired: false,
    created_at: new Date("2026-03-01"),
    test_cases: [
      { id: crypto.randomUUID(), content: "게시글 작성이 정상적으로 동작해야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }] },
      { id: crypto.randomUUID(), content: "채팅 기능이 정상적으로 동작해야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: false, error_reason: "페이지가 무한 로딩됨", is_resolved: false }] },
      { id: crypto.randomUUID(), content: "좋아요 기능이 정상적으로 동작해야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: true }, { id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }] },
      { id: crypto.randomUUID(), content: "검색 기능이 정상적으로 동작해야 한다.", feedbacks: [] },
      { id: crypto.randomUUID(), content: "회원가입 시 유효성 검사가 동작해야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: false, error_reason: "잘못된 데이터가 표시됨", is_resolved: false }, { id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }] },
      { id: crypto.randomUUID(), content: "알림 설정이 정상적으로 저장되어야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }] },
    ],
    tags: [{ name: "모바일" }, { name: "성능" }]
  },
  {
    title: "오늘의집",
    content: "오늘의집 서비스의 QA 테스트 프로젝트입니다. 주요 기능에 대한 피드백을 수집합니다.",
    url: "https://example.com/ohouse",
    expired_date: new Date("2026-11-30"),
    is_expired: false,
    created_at: new Date("2026-03-05"),
    test_cases: [
      { id: crypto.randomUUID(), content: "메인 페이지가 정상적으로 로딩되어야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }] },
      { id: crypto.randomUUID(), content: "이미지 업로드가 정상적으로 동작해야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }, { id: crypto.randomUUID(), is_ok: false, error_reason: "타임아웃 에러 발생", is_resolved: false }] },
      { id: crypto.randomUUID(), content: "댓글 작성이 정상적으로 동작해야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }] },
      { id: crypto.randomUUID(), content: "장바구니 추가가 정상적으로 동작해야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: false, error_reason: "버튼 클릭 시 반응이 없음", is_resolved: false }] },
      { id: crypto.randomUUID(), content: "결제 프로세스가 정상적으로 완료되어야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: true }, { id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }] },
      { id: crypto.randomUUID(), content: "공유 기능이 정상적으로 동작해야 한다.", feedbacks: [] },
      { id: crypto.randomUUID(), content: "다크모드 전환이 정상적으로 동작해야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }] },
      { id: crypto.randomUUID(), content: "로그아웃이 정상적으로 동작해야 한다.", feedbacks: [{ id: crypto.randomUUID(), is_ok: true, error_reason: null, is_resolved: false }, { id: crypto.randomUUID(), is_ok: false, error_reason: "500 에러 발생", is_resolved: false }] },
    ],
    tags: [{ name: "웹" }, { name: "UI" }, { name: "프론트엔드" }]
  }
])
```

```
db.projects.countDocuments()
```

결과로 10이 출력되야 함