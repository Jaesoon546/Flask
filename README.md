# Flask — 대전바이오융합 직업훈련

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=white)

Flask 웹 서버 실습입니다. Jinja 템플릿(`base.html` 상속), AJAX(JSON) 통신, MySQL 저장 프로시저로 성적 목록을 불러오는 페이지를 다룹니다.
성적 DB(`jsdb`)와 `student_select` 프로시저는 [MySQL 저장소](https://github.com/Jaesoon546/MySQL)의 `school_student/` 쿼리로 만든 것입니다.

```
Flask/
├── flaskserver.py        # Flask 앱 — 라우트 정의
├── dao/
│   └── sungjuk.py        # DB 접속 + student_select 프로시저 호출
├── templates/            # Jinja 템플릿 (모두 base.html 상속)
│   ├── base.html         # 공통 레이아웃 · 내비게이션 바
│   ├── index.html
│   ├── bootstrap/bootstrap.html
│   ├── javascript1.html
│   ├── ajax.html         # /_add_numbers 를 AJAX로 호출
│   ├── sungjuk.html      # 성적 목록 표
│   └── w3schools.html
└── static/images/ai.jpg
```

## 라우트

| 주소 | 내용 |
|---|---|
| `/view/<prod_name>`, `/info/<category>/<prod_name>` | URL 변수 받기 |
| `/index`, `/base`, `/bootstrap`, `/javascript1`, `/w3` | 템플릿 렌더링 |
| `/ajaxcall` → `/_add_numbers?a=&b=` | AJAX 요청, JSON 응답 (`jsonify`) |
| `/sungjuk_call` | DB에서 성적 목록을 받아 표로 출력 |

## 실행

```bash
pip install -r requirements.txt
export DB_HOST=<서버 IP>
export DB_PASSWORD=<비밀번호>
python flaskserver.py      # http://127.0.0.1:5000/index
```

DB 접속 정보는 공개 저장소에 올리지 않도록 환경변수로 받습니다.
