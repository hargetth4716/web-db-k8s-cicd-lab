import os
import psycopg2
from dotenv import load_dotenv

# .env 파일에서 환경변수 로드
load_dotenv()

def get_connection():
    """DB 연결 객체를 반환하는 함수"""
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "webdb"),
        user=os.getenv("DB_USER", "webuser"),
        password=os.getenv("DB_PASSWORD", "yourpassword")
    )
    return conn

def check_connection():
    """DB 연결 상태를 확인하는 함수"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"DB 연결 실패: {e}")
        return False