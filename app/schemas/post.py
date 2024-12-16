from datetime import datetime
from pydantic import BaseModel


class PostCreate(BaseModel):
    title: str
    content: str | None = None
    image_url: str | None = None
    published: bool

    class Config:
        orm_mode = True


class PostOut(PostCreate):
    pass