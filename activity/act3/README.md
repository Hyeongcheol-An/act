# Activity 2

## VM1

### 제출

- `VM1/docker-compose.yaml`
    - `flask.py` 구동
    - `apache` web server 구동
- `VM1/flask.py`
    - flask source code
    - port: 8080
    - VM2에 있는 DB와 연동
- `VM1/install.sh`
    - 패키지 설치 스크립트
- `VM1/README.md`
    - 설명

## VM2

- MySQL DB 설치
- Flask에서 MySQL DB 사용
    - INSERT, UPDATE, DELETE 기능 각각 하위 url로 생성 및 서비스 제공
    - 예: `ip:port/insert` 접근시 DB에 insert 기능 호출
    - 참고: https://www.fun-coding.org/mysql_basic6.html

### 제출

- `VM2/install.sh`
    - DB 및 라이브러리 패키지 설치 스크립트
- `VM2/README.md`
    - 설명