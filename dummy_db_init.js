// 사용 방법(Unix 계열 - Git Bash, WSL, Mac 등): docker compose -T exec mongo mongosh < dummy_db_init.js

// =====================================================
// 페이지 채우기용 더미 프로젝트 20개
// - 만료 프로젝트 5개 (25%)
// - 테스트 케이스 0~3개, 피드백 없음
// - user_id: str 타입으로 저장 (기존 백엔드 패턴 준수)
// =====================================================
use jungleqa;
db.projects.drop();
// =====================================================
// mongosh 복사 붙여넣기용 더미 데이터 삽입 스크립트 v3
// 수정사항:
//   - Feedback 구조 수정: { id, is_ok, error_reason, is_resolved }
//   - user_id: DB에서 직접 조회하여 참조
// =====================================================

const jungler = db.users.findOne({ login_id: "qwer1234" });
if (!jungler) { throw new Error("qwer1234 유저를 찾을 수 없습니다. 유저 컬렉션을 확인하세요."); }
print("✅ jungler _id: " + jungler._id);

// ──────────────────────────────────────────────────────────
// 프로젝트 1: 배달의민족 파트너센터 리뉴얼
//   - user_id: jungler (qwer1234)
//   - 테스트 케이스 8개, 케이스별 피드백 20개
//   - 성공률 다양하게 구성
// ──────────────────────────────────────────────────────────

const project1 = {
    _id: ObjectId(),
    user_id: jungler._id.toString(),
    title: "배달의민족 파트너센터 리뉴얼 - 사장님 대시보드 개편",
    content:
        "배달의민족 파트너센터의 사장님 대시보드를 전면 개편했습니다. " +
        "주요 변경사항: 실시간 주문 현황 위젯 추가, 매출 그래프 개선, 리뷰 관리 UI 개편, 메뉴 일괄 수정 기능 신설. " +
        "다양한 브라우저와 디바이스 환경에서 기능이 정상 동작하는지 테스트해 주세요.",
    url: "https://ceo-staging.baemin.com/dashboard",
    expired_date: new Date("2026-04-15"),
    is_expired: false,
    created_at: new Date("2026-03-06"),
    tags: [
        { name: "대시보드" },
        { name: "UI개편" },
        { name: "배달의민족" },
        { name: "파트너센터" },
    ],
    test_cases: [
        // ── TC1: 로그인 (거의 다 성공, 실패 1개) ──
        {
            id: ObjectId().toString(),
            content:
                "사장님 계정으로 로그인 후 대시보드 메인 페이지가 5초 이내에 정상 로드되는지 확인하세요. " +
                "(테스트 계정 ID: ceo_test@baemin.com / PW: Test1234!)",
            is_active: true,
            feedbacks: [
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "Samsung Internet 구버전에서 흰 화면만 표시되고 로드되지 않음", is_resolved: false },
            ],
        },

        // ── TC2: 실시간 주문 현황 위젯 (거의 다 성공, 실패 2개) ──
        {
            id: ObjectId().toString(),
            content:
                "대시보드 상단의 '실시간 주문 현황' 위젯에서 신규 주문 건수, 조리 중, 배달 중 건수가 " +
                "30초 이내 자동 갱신되는지 확인하세요. 페이지를 새로고침 없이 30초 대기 후 수치 변화를 관찰하세요.",
            is_active: true,
            feedbacks: [
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "25초 경과 후 위젯이 '연결 끊김' 오류를 표시하고 갱신 중단됨", is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "Firefox(Linux)에서 위젯 영역이 렌더링되지 않음, 빈 박스만 표시됨", is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
            ],
        },

        // ── TC3: 매출 그래프 기간 필터 (중간 성공률, 실패 9개) ──
        {
            id: ObjectId().toString(),
            content:
                "매출 그래프에서 기간 필터(오늘 / 7일 / 30일 / 직접 입력)를 각각 선택하여 " +
                "그래프 데이터가 해당 기간에 맞게 변경되는지 확인하세요. " +
                "직접 입력 시 2026-01-01 ~ 2026-02-28 구간을 입력해 보세요.",
            is_active: true,
            feedbacks: [
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "직접 입력 달력 팝업이 열리지 않음, 클릭해도 반응 없음", is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "30일 필터 선택 시 그래프가 빈 상태로 표시됨", is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "직접 입력 후 조회 버튼 클릭 시 500 에러 발생", is_resolved: true },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "모바일에서 날짜 직접 입력 UI가 잘려 보여 조회 불가", is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "Safari에서 30일 필터 클릭 시 페이지 전체가 새로고침됨", is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "시작일을 종료일보다 늦게 입력해도 오류 없이 빈 그래프가 표시됨", is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "그래프 툴팁이 화면 밖으로 벗어나 잘려 보임", is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "필터 변경 시 로딩 스피너가 사라지지 않고 계속 표시됨", is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "Edge에서 달력 UI가 깨져 보여 날짜 선택 불가", is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
            ],
        },

        // ── TC4: 리뷰 답글 작성 (거의 다 성공, 실패 1개) ──
        {
            id: ObjectId().toString(),
            content:
                "리뷰 관리 탭 진입 후, 첫 번째 리뷰에 답글을 작성하고 저장하세요. " +
                "저장 완료 후 답글이 목록에 즉시 반영되는지, 글자 수 제한(300자)이 정상 작동하는지 확인하세요.",
            is_active: true,
            feedbacks: [
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "이모지 포함 답글 저장 시 DB 오류 발생", is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
            ],
        },

        // ── TC5: 메뉴 일괄 수정 (조금 성공, 실패 14개) ──
        {
            id: ObjectId().toString(),
            content:
                "메뉴 관리 > 일괄 수정 탭에서 전체 메뉴 선택 후 가격을 일괄로 10% 인상하는 기능을 테스트하세요. " +
                "변경 전/후 가격이 정확히 계산되는지, 소수점 반올림 처리가 올바른지 확인하세요.",
            is_active: true,
            feedbacks: [
                { id: ObjectId().toString(), is_ok: false, error_reason: "일괄 수정 탭이 메뉴에 표시되지 않음", is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "전체 선택 체크박스 클릭해도 개별 메뉴 선택 안 됨", is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "10% 인상 적용 후 가격이 변경되지 않고 그대로 유지됨", is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "10,500원 10% 인상 시 11,550.0원으로 표시됨 (소수점 미제거)", is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "저장 버튼 클릭 시 '권한이 없습니다' 오류 팝업 발생", is_resolved: true },
                { id: ObjectId().toString(), is_ok: false, error_reason: "일괄 수정 후 일부 메뉴만 반영되고 나머지는 원래 가격 유지", is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "페이지 진입 시 로딩이 무한 반복되며 메뉴 목록이 표시되지 않음", is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "Safari에서 일괄 선택 후 '적용' 버튼이 비활성화 상태로 클릭 불가", is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "취소 버튼 클릭 시 변경사항이 취소되지 않고 그대로 저장됨", is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "메뉴 100개 이상 전체 선택 시 브라우저가 멈춤", is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "인상률 입력 필드에 음수 입력이 가능하고 유효성 검사 없음", is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "변경 완료 토스트 메시지가 나타나지 않음", is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "Edge에서 일괄 수정 탭 클릭 시 404 페이지로 이동", is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "가격 변경 이력이 히스토리 탭에 기록되지 않음", is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "모바일에서 체크박스가 너무 작아 터치 시 다른 메뉴가 선택됨", is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "특수문자 포함 메뉴명이 있을 때 일괄 저장 실패", is_resolved: false },
            ],
        },

        // ── TC6: 정산 내역 엑셀 다운로드 (중간 성공률, 실패 10개) ──
        {
            id: ObjectId().toString(),
            content:
                "정산 내역 탭에서 이번 달(2026년 3월) 정산 내역을 엑셀 파일로 다운로드하세요. " +
                "다운로드된 파일을 열어 컬럼 구성(날짜, 주문수, 총매출, 배달비, 실정산금)이 올바른지 확인하세요.",
            is_active: true,
            feedbacks: [
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "다운로드 클릭 시 빈 파일(0KB)이 저장됨", is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "실정산금 컬럼이 누락되어 있음", is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "Safari에서 다운로드 대신 브라우저에서 파일이 열려버림", is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "금액 셀이 텍스트 형식으로 저장되어 합계 계산 불가", is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "3월 데이터 조회 시 2월 데이터까지 포함되어 다운로드됨", is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "파일명이 'export.xlsx'로 고정되어 날짜 정보가 없음", is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "다운로드 버튼 클릭 후 10초 이상 응답 없음, 타임아웃 발생", is_resolved: true },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "한글 인코딩 깨짐, 가게명이 '???' 으로 표시됨", is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "주문 수 컬럼 값이 모두 0으로 표시됨", is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
            ],
        },

        // ── TC7: 알림 설정 저장 (거의 다 성공, 실패 2개) ──
        {
            id: ObjectId().toString(),
            content:
                "설정 > 알림 탭에서 '신규 주문 알림'과 '리뷰 등록 알림'을 ON으로, '마케팅 알림'을 OFF로 설정한 뒤 저장하세요. " +
                "페이지를 새로고침한 후 설정값이 그대로 유지되는지 확인하세요.",
            is_active: true,
            feedbacks: [
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "저장 후 새로고침 시 마케팅 알림이 다시 ON으로 초기화됨", is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "토글 변경 즉시 저장되는 방식인데 실수로 변경 시 되돌리기 수단이 없음", is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
            ],
        },

        // ── TC8: 공지사항 팝업 (전부 성공) ──
        {
            id: ObjectId().toString(),
            content:
                "대시보드 최초 로그인 시 공지사항 팝업이 자동으로 표시되는지 확인하세요. " +
                "'오늘 하루 보지 않기' 체크 후 닫고 재로그인 시 해당 날에는 팝업이 나타나지 않는지도 확인하세요.",
            is_active: true,
            feedbacks: [
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
            ],
        },
    ],
};

// ──────────────────────────────────────────────────────────
// 프로젝트 2: 네이버 스마트스토어 - 재고 관리 모듈
//   - user_id: qwer1234 가 아닌 별도 유저
//   - 테스트 케이스 6개, 케이스별 피드백 5개, 실패 케이스 2개
// ──────────────────────────────────────────────────────────

const project2 = {
    _id: ObjectId(),
    user_id: ObjectId(),
    title: "네이버 스마트스토어 판매자 어드민 - 재고 관리 모듈 신규 개발",
    content:
        "스마트스토어 판매자 어드민에 재고 관리 모듈을 신규 개발했습니다. " +
        "주요 기능: 상품별 재고 수량 등록/수정, 재고 부족 알림 임계값 설정, 재고 이력 조회, " +
        "옵션별 재고 분리 관리, 엑셀 대량 업로드. " +
        "실제 판매자 시나리오를 기준으로 테스트해 주세요.",
    url: "https://sell.smartstore.naver.com/inventory-staging",
    expired_date: new Date("2026-04-30"),
    is_expired: false,
    created_at: new Date("2026-03-05"),
    tags: [
        { name: "재고관리" },
        { name: "스마트스토어" },
        { name: "네이버" },
        { name: "판매자어드민" },
        { name: "신규기능" },
    ],
    test_cases: [
        {
            id: ObjectId().toString(),
            content:
                "재고 관리 탭에서 임의 상품을 선택 후 재고 수량을 50으로 입력하고 저장하세요. " +
                "저장 완료 후 상품 목록에서 해당 상품의 재고가 50으로 표시되는지 확인하세요.",
            is_active: true,
            feedbacks: [
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
            ],
        },
        {
            id: ObjectId().toString(),
            content:
                "재고 알림 설정에서 알림 발송 임계값을 10으로 설정하세요. " +
                "이후 해당 상품의 재고를 9로 변경했을 때 대시보드 알림 아이콘에 재고 부족 알림이 발생하는지 확인하세요.",
            is_active: true,
            feedbacks: [
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "재고를 9로 변경해도 알림이 즉시 발생하지 않음, 새로고침 후에야 표시됨", is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
            ],
        },
        {
            id: ObjectId().toString(),
            content:
                "재고 이력 탭에서 특정 상품의 최근 1주일 재고 변동 이력을 조회하세요. " +
                "이력에 변경일시, 변경 전 수량, 변경 후 수량, 변경 사유가 포함되어 있는지 확인하세요.",
            is_active: true,
            feedbacks: [
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
            ],
        },
        {
            id: ObjectId().toString(),
            content:
                "옵션이 있는 상품(예: 색상 3가지 × 사이즈 3가지 = 9개 옵션)을 선택하여 " +
                "각 옵션별로 다른 재고 수량(10, 20, 5 등)을 입력하고 저장하세요. " +
                "저장 후 옵션별로 재고가 분리되어 표시되는지 확인하세요.",
            is_active: true,
            feedbacks: [
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: false, error_reason: "옵션이 9개 이상일 때 저장 시 일부 옵션 재고가 0으로 초기화됨", is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
            ],
        },
        {
            id: ObjectId().toString(),
            content:
                "재고 관리 > 대량 업로드 탭에서 제공된 엑셀 템플릿을 다운로드하고, " +
                "상품 ID와 재고 수량을 입력한 뒤 업로드하세요. " +
                "업로드 완료 후 각 상품의 재고가 정상 반영되는지 확인하세요.",
            is_active: true,
            feedbacks: [
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
            ],
        },
        {
            id: ObjectId().toString(),
            content:
                "특정 상품의 재고를 0으로 변경하고 저장하세요. " +
                "스마트스토어 상품 상세 페이지에서 해당 상품이 '품절' 상태로 자동 변경되었는지 확인하세요.",
            is_active: true,
            feedbacks: [
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
                { id: ObjectId().toString(), is_ok: true, error_reason: null, is_resolved: false },
            ],
        },
    ],
};

// ──────────────────────────────────────────────────────────
// 삽입 실행
// ──────────────────────────────────────────────────────────

db.projects.insertMany([project1, project2]);

print("✅ 더미 데이터 삽입 완료!");
print("  - 프로젝트 1 (배달의민족): " + project1._id);
print("  - 프로젝트 2 (네이버 스마트스토어): " + project2._id);

db.projects.insertMany([

    // ── 1. 현대모비스 (만료) ──
    {
        _id: ObjectId(),
        user_id: "a1b2c3d4e5f6a1b2c3d4e5f1",
        title: "현대모비스 딜러사 부품 재고 조회 포털 UI 개편",
        content: "딜러사 전용 부품 재고 조회 포털의 인터페이스를 전면 개편했습니다. 실시간 재고 현황 조회, 긴급 발주 요청, 배송 추적 기능을 테스트해 주세요.",
        url: "https://partnerportal-staging.mobis.co.kr/inventory",
        expired_date: new Date("2026-01-20"),
        is_expired: true,
        created_at: new Date("2026-01-05"),
        tags: [{ name: "현대모비스" }, { name: "포털" }, { name: "재고조회" }],
        test_cases: [
            { id: ObjectId().toString(), content: "딜러사 계정으로 로그인 후 담당 지역 부품 재고 목록이 정상 조회되는지 확인", is_active: true, feedbacks: [] },
            { id: ObjectId().toString(), content: "긴급 발주 요청 후 담당 영업사원에게 알림이 발송되는지 확인", is_active: true, feedbacks: [] },
        ],
    },

    // ── 2. 초록우산 어린이재단 (만료) ──
    {
        _id: ObjectId(),
        user_id: "a1b2c3d4e5f6a1b2c3d4e5f2",
        title: "초록우산 어린이재단 정기후원 관리 페이지 개편",
        content: "정기후원자가 후원 금액 변경, 일시 정지, 해지를 직접 처리할 수 있는 셀프서비스 페이지를 새로 만들었습니다. 각 기능의 정상 동작 여부를 테스트해 주세요.",
        url: "https://my-staging.childfund.or.kr/donation",
        expired_date: new Date("2026-02-10"),
        is_expired: true,
        created_at: new Date("2026-01-25"),
        tags: [{ name: "초록우산" }, { name: "후원관리" }, { name: "비영리" }],
        test_cases: [
            { id: ObjectId().toString(), content: "정기후원 금액을 월 3만원에서 5만원으로 변경하고 다음 결제일에 반영되는지 확인", is_active: true, feedbacks: [] },
            { id: ObjectId().toString(), content: "후원 일시 정지 신청 후 정지 확인 이메일이 발송되는지 확인", is_active: true, feedbacks: [] },
            { id: ObjectId().toString(), content: "후원 해지 신청 시 확인 모달이 표시되는지 확인", is_active: true, feedbacks: [] },
        ],
    },

    // ── 3. 카카오페이 (만료) ──
    {
        _id: ObjectId(),
        user_id: "a1b2c3d4e5f6a1b2c3d4e5f3",
        title: "카카오페이 청구서 간편결제 - 공과금 자동 등록 기능",
        content: "전기, 수도, 가스 등 공과금 청구서를 카카오페이에 자동 등록하고 납부 기한 전 알림을 받는 기능입니다. 청구서 등록 및 알림 수신 흐름을 테스트해 주세요.",
        url: "https://bill-staging.kakaopay.com/auto-register",
        expired_date: new Date("2026-02-28"),
        is_expired: true,
        created_at: new Date("2026-02-10"),
        tags: [{ name: "카카오페이" }, { name: "청구서" }, { name: "간편결제" }],
        test_cases: [
            { id: ObjectId().toString(), content: "한국전력 고객번호 입력 후 청구서가 자동 등록되는지 확인", is_active: true, feedbacks: [] },
        ],
    },

    // ── 4. 대한적십자사 (만료) ──
    {
        _id: ObjectId(),
        user_id: "a1b2c3d4e5f6a1b2c3d4e5f4",
        title: "대한적십자사 헌혈 예약 시스템 앱 리뉴얼",
        content: "헌혈 예약 앱을 전면 리뉴얼했습니다. 헌혈 가능 여부 자가 문진, 헌혈 센터 예약, 헌혈증 디지털 발급 기능을 테스트해 주세요.",
        url: "https://bloodapp-staging.redcross.or.kr",
        expired_date: new Date("2026-02-20"),
        is_expired: true,
        created_at: new Date("2026-02-01"),
        tags: [{ name: "적십자" }, { name: "헌혈" }, { name: "앱리뉴얼" }],
        test_cases: [
            { id: ObjectId().toString(), content: "자가 문진 10문항 완료 후 헌혈 가능 여부 결과 화면이 정상 표시되는지 확인", is_active: true, feedbacks: [] },
            { id: ObjectId().toString(), content: "헌혈 센터 예약 완료 후 카카오톡으로 예약 확인 메시지가 발송되는지 확인", is_active: true, feedbacks: [] },
        ],
    },

    // ── 5. 현대해상 (만료) ──
    {
        _id: ObjectId(),
        user_id: "a1b2c3d4e5f6a1b2c3d4e5f5",
        title: "현대해상 다이렉트 자동차보험 간편 갱신 플로우 개선",
        content: "만기 도래 고객이 앱에서 3단계 이내로 자동차보험을 갱신할 수 있도록 플로우를 개선했습니다. 갱신 견적 조회부터 결제 완료까지의 흐름을 테스트해 주세요.",
        url: "https://direct-staging.hi.co.kr/renewal",
        expired_date: new Date("2026-03-01"),
        is_expired: true,
        created_at: new Date("2026-02-15"),
        tags: [{ name: "현대해상" }, { name: "자동차보험" }, { name: "갱신" }],
        test_cases: [
            { id: ObjectId().toString(), content: "기존 계약 정보가 자동 불러와져 갱신 견적이 1단계에서 바로 표시되는지 확인", is_active: true, feedbacks: [] },
            { id: ObjectId().toString(), content: "카드 간편결제로 보험료 납부 완료 후 증권 PDF가 이메일로 발송되는지 확인", is_active: true, feedbacks: [] },
        ],
    },

    // ── 6. 네이버 클라우드 ──
    {
        _id: ObjectId(),
        user_id: "a1b2c3d4e5f6a1b2c3d4e5f6",
        title: "네이버 클라우드 플랫폼 - Object Storage 웹 콘솔 파일 관리 개편",
        content: "Object Storage 웹 콘솔에서 파일 업로드, 폴더 생성, 권한 설정을 드래그앤드롭으로 처리할 수 있도록 개편했습니다. 대용량 파일 업로드 및 권한 설정 기능을 테스트해 주세요.",
        url: "https://console-staging.ncloud.com/object-storage",
        expired_date: new Date("2026-04-10"),
        is_expired: false,
        created_at: new Date("2026-03-01"),
        tags: [{ name: "네이버클라우드" }, { name: "ObjectStorage" }, { name: "콘솔" }],
        test_cases: [
            { id: ObjectId().toString(), content: "1GB 이상 파일 드래그앤드롭 업로드 시 진행률 표시 및 완료 알림이 정상 동작하는지 확인", is_active: true, feedbacks: [] },
            { id: ObjectId().toString(), content: "버킷 권한을 '공개'로 변경 후 외부에서 URL로 파일 접근이 가능한지 확인", is_active: true, feedbacks: [] },
        ],
    },

    // ── 7. 쿠팡 ──
    {
        _id: ObjectId(),
        user_id: "a1b2c3d4e5f6a1b2c3d4e5f7",
        title: "쿠팡 로켓배송 실시간 배송 현황 지도 뷰 신규 개발",
        content: "주문 상세 페이지에서 배송 기사의 현재 위치와 예상 도착 시간을 지도로 확인할 수 있는 기능을 새로 개발했습니다. 실시간 위치 갱신 및 도착 알림을 테스트해 주세요.",
        url: "https://order-staging.coupang.com/delivery-map",
        expired_date: new Date("2026-04-20"),
        is_expired: false,
        created_at: new Date("2026-03-02"),
        tags: [{ name: "쿠팡" }, { name: "로켓배송" }, { name: "실시간지도" }],
        test_cases: [
            { id: ObjectId().toString(), content: "배송 출발 후 지도 뷰에서 배송 기사 위치가 30초 이내 갱신되는지 확인", is_active: true, feedbacks: [] },
            { id: ObjectId().toString(), content: "배송 완료 시 앱 푸시 알림과 함께 지도 뷰가 '배송 완료' 상태로 전환되는지 확인", is_active: true, feedbacks: [] },
        ],
    },

    // ── 8. 토스 ──
    {
        _id: ObjectId(),
        user_id: "a1b2c3d4e5f6a1b2c3d4e5f8",
        title: "토스 가계부 - 소비 패턴 AI 리포트 기능 베타",
        content: "월간 소비 내역을 분석해 카테고리별 소비 패턴과 절약 팁을 제공하는 AI 리포트 기능 베타 버전입니다. 리포트 생성 정확도와 UI 가독성을 테스트해 주세요.",
        url: "https://app-staging.toss.im/report/ai",
        expired_date: new Date("2026-05-01"),
        is_expired: false,
        created_at: new Date("2026-03-03"),
        tags: [{ name: "토스" }, { name: "가계부" }, { name: "AI리포트" }],
        test_cases: [
            { id: ObjectId().toString(), content: "최근 3개월 소비 내역 기반 AI 리포트가 1분 이내 생성되는지 확인", is_active: true, feedbacks: [] },
        ],
    },

    // ── 9. 카카오맵 ──
    {
        _id: ObjectId(),
        user_id: "a1b2c3d4e5f6a1b2c3d4e5f9",
        title: "카카오맵 즐겨찾기 폴더 공유 기능 신규 개발",
        content: "카카오맵 즐겨찾기 폴더를 특정 친구 또는 링크로 공유할 수 있는 기능입니다. 공유 수신자가 폴더를 저장하거나 지도에서 확인하는 흐름을 테스트해 주세요.",
        url: "https://map-staging.kakao.com/favorite/share",
        expired_date: new Date("2026-04-25"),
        is_expired: false,
        created_at: new Date("2026-02-28"),
        tags: [{ name: "카카오맵" }, { name: "즐겨찾기" }, { name: "공유" }],
        test_cases: [
            { id: ObjectId().toString(), content: "즐겨찾기 폴더 공유 링크 생성 후 비로그인 상태에서 링크 접근 시 지도 뷰로 정상 열리는지 확인", is_active: true, feedbacks: [] },
            { id: ObjectId().toString(), content: "공유받은 폴더를 내 즐겨찾기에 저장 후 목록에 정상 추가되는지 확인", is_active: true, feedbacks: [] },
        ],
    },

    // ── 10. 당근마켓 ──
    {
        _id: ObjectId(),
        user_id: "a1b2c3d4e5f6a1b2c3d4e502",
        title: "당근마켓 안전결제 - 직거래 보호 에스크로 서비스 도입",
        content: "직거래 시 구매자가 안전결제로 송금하면 거래 완료 확인 후 판매자에게 정산되는 에스크로 서비스를 도입했습니다. 결제, 확인, 정산 흐름을 테스트해 주세요.",
        url: "https://pay-staging.daangn.com/escrow",
        expired_date: new Date("2026-05-10"),
        is_expired: false,
        created_at: new Date("2026-03-04"),
        tags: [{ name: "당근마켓" }, { name: "안전결제" }, { name: "에스크로" }],
        test_cases: [
            { id: ObjectId().toString(), content: "구매자가 안전결제로 송금 후 판매자 앱에 '결제 대기 중' 상태가 표시되는지 확인", is_active: true, feedbacks: [] },
            { id: ObjectId().toString(), content: "구매자가 거래 완료 확인 후 24시간 이내 판매자 계좌로 정산되는지 확인", is_active: true, feedbacks: [] },
            { id: ObjectId().toString(), content: "구매자가 7일 이내 확인을 안 할 경우 자동 정산이 진행되는지 확인", is_active: true, feedbacks: [] },
        ],
    },

    // ── 11. 올리브영 ──
    {
        _id: ObjectId(),
        user_id: "a1b2c3d4e5f6a1b2c3d4e503",
        title: "올리브영 온라인몰 - 피부 타입별 맞춤 상품 추천 필터 개편",
        content: "피부 타입, 고민, 성분 선호도를 입력하면 맞춤 상품을 추천해주는 필터 기능을 개편했습니다. 필터 조합별 추천 결과의 정확도와 응답 속도를 테스트해 주세요.",
        url: "https://www-staging.oliveyoung.co.kr/recommend",
        expired_date: new Date("2026-04-30"),
        is_expired: false,
        created_at: new Date("2026-03-01"),
        tags: [{ name: "올리브영" }, { name: "상품추천" }, { name: "피부타입" }],
        test_cases: [
            { id: ObjectId().toString(), content: "'지성, 모공, 무향' 조건 선택 후 추천 상품 20개가 3초 이내 표시되는지 확인", is_active: true, feedbacks: [] },
        ],
    },

    // ── 12. 무신사 ──
    {
        _id: ObjectId(),
        user_id: "a1b2c3d4e5f6a1b2c3d4e504",
        title: "무신사 스토어 - 코디 저장 및 SNS 공유 기능 신규 개발",
        content: "상품 상세 페이지에서 '코디에 추가' 버튼으로 나만의 코디를 구성하고 SNS로 공유할 수 있는 기능입니다. 코디 저장, 편집, 공유 흐름을 테스트해 주세요.",
        url: "https://www-staging.musinsa.com/codi",
        expired_date: new Date("2026-06-01"),
        is_expired: false,
        created_at: new Date("2026-03-03"),
        tags: [{ name: "무신사" }, { name: "코디" }, { name: "SNS공유" }],
        test_cases: [
            { id: ObjectId().toString(), content: "상품 3개 이상 추가하여 코디 저장 후 '내 코디' 목록에 정상 표시되는지 확인", is_active: true, feedbacks: [] },
            { id: ObjectId().toString(), content: "코디 공유 링크 생성 후 비로그인 상태에서 접근 시 코디 상세 페이지가 열리는지 확인", is_active: true, feedbacks: [] },
        ],
    },

    // ── 13. 야놀자 ──
    {
        _id: ObjectId(),
        user_id: "a1b2c3d4e5f6a1b2c3d4e505",
        title: "야놀자 숙소 예약 취소 환불 자동화 프로세스 개선",
        content: "취소 정책에 따라 환불 금액을 자동 계산하고 즉시 환불 처리하는 프로세스를 개선했습니다. 취소 시점별 환불 금액 계산 정확도를 테스트해 주세요.",
        url: "https://booking-staging.yanolja.com/cancel",
        expired_date: new Date("2026-04-15"),
        is_expired: false,
        created_at: new Date("2026-02-25"),
        tags: [{ name: "야놀자" }, { name: "예약취소" }, { name: "환불자동화" }],
        test_cases: [
            { id: ObjectId().toString(), content: "체크인 3일 전 취소 시 70% 환불 정책이 정확히 적용되는지 확인", is_active: true, feedbacks: [] },
            { id: ObjectId().toString(), content: "당일 취소 시 환불 불가 안내 모달이 표시되고 취소 버튼이 비활성화되는지 확인", is_active: true, feedbacks: [] },
        ],
    },

    // ── 14. KB국민은행 ──
    {
        _id: ObjectId(),
        user_id: "a1b2c3d4e5f6a1b2c3d4e506",
        title: "KB스타뱅킹 - 외화 환전 예약 서비스 신규 개발",
        content: "원하는 환율에 도달했을 때 자동으로 환전이 실행되는 환전 예약 서비스를 개발했습니다. 환율 알림 등록, 자동 환전 실행, 환전 내역 조회 기능을 테스트해 주세요.",
        url: "https://app-staging.kbstar.com/exchange/reserve",
        expired_date: new Date("2026-05-20"),
        is_expired: false,
        created_at: new Date("2026-03-03"),
        tags: [{ name: "KB국민은행" }, { name: "환전" }, { name: "예약서비스" }],
        test_cases: [
            { id: ObjectId().toString(), content: "USD 환율 목표가 설정 후 해당 환율 도달 시 카카오톡 알림이 발송되는지 확인", is_active: true, feedbacks: [] },
        ],
    },

    // ── 15. 신한카드 ──
    {
        _id: ObjectId(),
        user_id: "a1b2c3d4e5f6a1b2c3d4e507",
        title: "신한카드 MY PAGE - 할부 일시불 전환 셀프 서비스",
        content: "진행 중인 할부를 일시불로 전환하거나 남은 할부금을 조기 상환할 수 있는 셀프 서비스 기능입니다. 전환 수수료 계산 정확도와 처리 결과를 테스트해 주세요.",
        url: "https://mypage-staging.shinhancard.com/installment",
        expired_date: new Date("2026-04-05"),
        is_expired: false,
        created_at: new Date("2026-02-20"),
        tags: [{ name: "신한카드" }, { name: "할부전환" }, { name: "마이페이지" }],
        test_cases: [
            { id: ObjectId().toString(), content: "12개월 할부 중 6개월 경과 시점에서 일시불 전환 수수료가 정확히 계산되는지 확인", is_active: true, feedbacks: [] },
            { id: ObjectId().toString(), content: "전환 완료 후 다음 결제일 청구 예정 금액이 즉시 업데이트되는지 확인", is_active: true, feedbacks: [] },
        ],
    },

    // ── 16. 배달의민족 단체 주문 ──
    {
        _id: ObjectId(),
        user_id: "a1b2c3d4e5f6a1b2c3d4e508",
        title: "배달의민족 - 단체 주문 및 공동 결제 기능 신규 개발",
        content: "팀 또는 가족 단위로 각자 메뉴를 담고 한 번에 결제할 수 있는 단체 주문 기능입니다. 주문 링크 공유, 메뉴 취합, 공동 결제 흐름을 테스트해 주세요. iOS와 Android, 다양한 크기의 패드나 스마트폰의 테스트가 필요합니다. 테스트에 참여해주신 분들께는 추첨을 통해 배달의민족 상품권을 드립니다!",
        url: "https://order-staging.baemin.com/group",
        expired_date: new Date("2026-05-15"),
        is_expired: false,
        created_at: new Date("2026-03-04"),
        tags: [{ name: "배달의민족" }, { name: "단체주문" }, { name: "공동결제" }],
        test_cases: [
            { id: ObjectId().toString(), content: "주문 링크 생성 후 최대 10명이 각자 메뉴를 담은 뒤 주문자에게 취합 알림이 오는지 확인", is_active: true, feedbacks: [] },
            { id: ObjectId().toString(), content: "공동 결제 시 참여자별 금액이 정확히 분할되어 표시되는지 확인", is_active: true, feedbacks: [] },
        ],
    },

    // ── 17. 카카오T 주차 ──
    {
        _id: ObjectId(),
        user_id: "a1b2c3d4e5f6a1b2c3d4e509",
        title: "카카오T 주차 - 월정기권 자동 연장 및 결제 기능",
        content: "월정기 주차권 만료일 전 자동 결제로 연장되는 기능을 개발했습니다. 자동 연장 설정, 결제 실패 시 재시도, 연장 내역 조회 흐름을 테스트해 주세요.",
        url: "https://parking-staging.kakao.com/monthly/auto-renew",
        expired_date: new Date("2026-04-30"),
        is_expired: false,
        created_at: new Date("2026-03-02"),
        tags: [{ name: "카카오T" }, { name: "주차" }, { name: "정기권" }],
        test_cases: [],
    },

    // ── 18. 네이버웹툰 ──
    {
        _id: ObjectId(),
        user_id: "a1b2c3d4e5f6a1b2c3d4e510",
        title: "네이버웹툰 - 오프라인 저장 및 이어보기 기능 개선",
        content: "미리 다운로드한 회차를 오프라인 환경에서 이어볼 수 있는 기능을 개선했습니다. 저장 용량 관리, 오프라인 재생, 읽음 동기화 흐름을 테스트해 주세요.",
        url: "https://app-staging.webtoon.naver.com/offline",
        expired_date: new Date("2026-06-10"),
        is_expired: false,
        created_at: new Date("2026-03-03"),
        tags: [{ name: "네이버웹툰" }, { name: "오프라인" }, { name: "이어보기" }],
        test_cases: [
            { id: ObjectId().toString(), content: "Wi-Fi 환경에서 10회차 다운로드 후 비행기 모드로 전환하여 정상 재생되는지 확인", is_active: true, feedbacks: [] },
        ],
    },

    // ── 19. 위버스 ──
    {
        _id: ObjectId(),
        user_id: "a1b2c3d4e5f6a1b2c3d4e511",
        title: "위버스 - 팬 커뮤니티 실시간 투표 기능 신규 개발",
        content: "아티스트가 팬들을 대상으로 실시간 투표를 열고 결과를 즉시 공유할 수 있는 기능입니다. 투표 생성, 참여, 실시간 결과 표시 흐름을 테스트해 주세요.",
        url: "https://weverse-staging.hybe.com/vote",
        expired_date: new Date("2026-05-25"),
        is_expired: false,
        created_at: new Date("2026-03-03"),
        tags: [{ name: "위버스" }, { name: "팬커뮤니티" }, { name: "실시간투표" }],
        test_cases: [
            { id: ObjectId().toString(), content: "투표 생성 후 팬 계정으로 참여 시 실시간 결과 그래프가 즉시 업데이트되는지 확인", is_active: true, feedbacks: [] },
            { id: ObjectId().toString(), content: "투표 종료 후 결과 페이지가 아카이브로 보존되고 재조회 가능한지 확인", is_active: true, feedbacks: [] },
        ],
    },

    // ── 20. 국민건강보험공단 ──
    {
        _id: ObjectId(),
        user_id: "a1b2c3d4e5f6a1b2c3d4e512",
        title: "국민건강보험 The건강보험 앱 - 건강검진 결과 AI 해설 기능",
        content: "건강검진 결과지를 업로드하면 각 항목의 의미와 주의사항을 쉬운 언어로 해설해주는 AI 기능입니다. 결과 해설 정확도, 이상 수치 강조 표시, 병원 연계 안내 흐름을 테스트해 주세요.",
        url: "https://app-staging.nhis.or.kr/checkup/ai-explain",
        expired_date: new Date("2026-07-01"),
        is_expired: false,
        created_at: new Date("2026-03-03"),
        tags: [{ name: "건강보험공단" }, { name: "건강검진" }, { name: "AI해설" }],
        test_cases: [
            { id: ObjectId().toString(), content: "이상 수치 포함된 검진 결과 업로드 시 해당 항목이 강조 표시되고 해설이 표시되는지 확인", is_active: true, feedbacks: [] },
            { id: ObjectId().toString(), content: "'전문의 상담 연계' 버튼 클릭 시 관련 진료과 병원 목록이 현재 위치 기반으로 표시되는지 확인", is_active: true, feedbacks: [] },
        ],
    },

    // -- 21. Krafton 정글 SW/AI랩 --
    {
        _id: ObjectId(),
        user_id: "b3c4d5e6f7a8b3c4d5e6f7a1",
        title: "Krafton 정글 SW/AI랩 - 개발자 역량 평가 플랫폼 베타",
        content: "크래프톤 정글 SW/AI랩에서 개발한 개발자 역량 평가 플랫폼 베타 버전입니다. " +
            "알고리즘 문제 풀이, 코드 리뷰, AI 기반 피드백 생성까지 통합된 평가 흐름을 제공합니다. " +
            "문제 출제 및 제출, 채점 결과 표시, AI 피드백 생성 기능을 테스트해 주세요.",
        url: "https://jungle-staging.krafton.com/eval",
        expired_date: new Date("2026-05-31"),
        is_expired: false,
        created_at: new Date("2026-03-04"),
        tags: [{ name: "크래프톤" }, { name: "정글" }, { name: "역량평가" }, { name: "AI피드백" }],
        test_cases: [
            {
                id: ObjectId().toString(),
                content: "알고리즘 문제 제출 후 채점 결과(정답/오답/시간초과)가 10초 이내 표시되는지 확인",
                is_active: true,
                feedbacks: []
            },
            {
                id: ObjectId().toString(),
                content: "채점 완료 후 AI 피드백이 자동 생성되어 코드 개선 제안이 표시되는지 확인",
                is_active: true,
                feedbacks: []
            },
        ],
    },

]);

print("✅ 페이지 채우기용 더미 프로젝트 20개 삽입 완료!");
print("   만료 프로젝트 5개: 현대모비스, 초록우산, 카카오페이, 대한적십자사, 현대해상");
print("   활성 프로젝트 15개");