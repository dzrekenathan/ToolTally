from fastapi import APIRouter, Depends, HTTPException, UploadFile, status
from fastapi.responses import JSONResponse
from httpx import post
from sqlalchemy.orm import Session

from app import schemas
from app.core.database import get_db
from app.models import models
from app.schemas.post import PostCreate, PostOut


router = APIRouter(tags=["posts"])

@router.get("/posts", status_code=status.HTTP_200_OK, response_model=list[PostOut])
async def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()

    if posts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Posts not found")

    return posts


@router.get("/posts/{id}", status_code=status.HTTP_200_OK, response_model=PostOut)
async def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()

    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    return post


@router.post("/posts", status_code=status.HTTP_201_CREATED, response_model=PostOut)
async def create_post(post: PostCreate, db: Session = Depends(get_db), file: UploadFile = None):
    
    if file.content_type != "image/jpeg" and file.content_type != "image/png":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid file type")

    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    post_query.delete(synchronize_session=False)
    db.commit()

    return

@router.put("/posts/{id}", status_code=status.HTTP_200_OK, response_model=PostOut)
async def update_post(id: int, post: PostCreate, db: Session = Depends(get_db)):
    """
    Updates a post with the given id. If the post does not exist, returns a 404.

    Args:
        id (int): The id of the post to update.
        post (PostCreate): The new post data.

    Returns:
        None
    """
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    post_query.update(post.dict(), synchronize_session=False)
    db.commit()

    return