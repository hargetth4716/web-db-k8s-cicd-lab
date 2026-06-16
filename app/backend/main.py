from fastapi import FastAPI, HTTPException
from database import get_connection, check_connection
from models import PostCreate, PostResponse
from typing import List

app = FastAPI(
    title="web-db-k8s-cicd-lab API",
    description="DevOps 포트폴리오 실습용 Backend API",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    """서버 상태 확인 API"""
    return {"status": "ok", "message": "server is running"}

@app.get("/db-check")
def db_check():
    """DB 연결 상태 확인 API"""
    if check_connection():
        return {"status": "ok", "message": "database connected"}
    raise HTTPException(status_code=500, detail="database connection failed")

@app.get("/posts", response_model=List[PostResponse])
def get_posts():
    """게시글 목록 조회 API"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, content, created_at FROM posts ORDER BY id DESC")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return [
        PostResponse(id=row[0], title=row[1], content=row[2], created_at=row[3])
        for row in rows
    ]

@app.post("/posts", response_model=PostResponse)
def create_post(post: PostCreate):
    """게시글 생성 API"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO posts (title, content) VALUES (%s, %s) RETURNING id, title, content, created_at",
        (post.title, post.content)
    )
    row = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()

    return PostResponse(id=row[0], title=row[1], content=row[2], created_at=row[3])