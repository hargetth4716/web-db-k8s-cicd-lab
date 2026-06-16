# 베이스 이미지: Python 3.11 슬림 버전
# 슬림 버전은 불필요한 패키지를 제거해서 이미지 크기가 작음
FROM python:3.11-slim

# 컨테이너 안에서 작업할 디렉터리 설정
WORKDIR /app

# 패키지 목록 먼저 복사 후 설치
# requirements.txt만 먼저 복사하는 이유는 캐시 활용 때문
# 코드가 바뀌어도 패키지가 안 바뀌면 이 레이어는 다시 빌드하지 않음
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 나머지 코드 복사
COPY . .

# 컨테이너가 사용할 포트 명시 (실제 포트 오픈은 docker-compose에서)
EXPOSE 8000

# 컨테이너 시작 시 실행할 명령어
# uvicorn으로 FastAPI 앱 실행
# 0.0.0.0은 컨테이너 외부에서 접근 가능하도록 모든 인터페이스에 바인딩
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]