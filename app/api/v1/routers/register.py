from fastapi import Depends, APIRouter, HTTPException, status
from app.core.authentication.hashing import hash_password
from app.core.database import get_db
from app.models import models
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut
from app.core.authentication.auth_middleware import get_current_active_user, get_current_user


router = APIRouter(
    tags=["register"],
    responses={404: {"description": "Not found"}},
)


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=UserOut)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):

    hashed_password = hash_password(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user