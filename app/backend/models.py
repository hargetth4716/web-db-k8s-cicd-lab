from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PostCreate(BaseModel):
    """게시글 생성할 때 받는 데이터 구조"""
    title: str
    content: str

class PostResponse(BaseModel):
    """게시글 조회할 때 반환하는 데이터 구조"""
    id: int
    title: str
    content: str
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True