# Flask 명언 저장 웹앱

간단한 Flask 기반의 웹 애플리케이션으로, 사용자가 명언을 입력하고 저장할 수 있는 미니 프로젝트.
flask 복습하려고 만들었음

## 🛠 사용 기술

- Python 3
- Flask
- SQLite3

## ✨ 주요 기능

- 명언 입력 및 저장
- 저장된 명언 목록 보기
- SQLite를 통한 간단한 데이터 저장 

## 🗂 프로젝트 구조

flask_tutorial/ \\
├── app.py # Flask 애플리케이션 메인 \\
├── schema.sql # SQLite 초기 테이블 생성 \\
├── templates/ \\
│ ├── index.html # 명언 입력 폼 \\
│ └── quotes.html # 명언 목록 출력 \\

## ⚙️ 실행 방법

1. 저장소 클론 및 폴더 이동
   git clone https://github.com/yourusername/random_quote.git
   cd flask_tutorial
   
3. 가상환경 생성 및 Flask 설치
   python -m venv venv
   source venv/bin/activate  # Windows는 venv\Scripts\activate

4. 앱 실행
   python app.py
