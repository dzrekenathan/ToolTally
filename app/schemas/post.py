from datetime import datetime
from pydantic import BaseModel


class PostCreate(BaseModel):
    id: int
    title: str
    content: str | None = None
    image_url: str | None = None
    published: bool
    date_created: datetime

    class Config:
        orm_mode = True


class PostOut(PostCreate):
    pass