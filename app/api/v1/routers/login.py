from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.core.authentication.auth_token import create_access_token
from app.core.authentication.hashing import verify
from app.core.database import get_db
from app.models import models
from app.schemas.token import Token
from app.schemas.user import UserCreate, UserOut
from app.core.authentication.auth_middleware import get_current_active_user


router = APIRouter()


@router.post("/login", status_code=status.HTTP_200_OK)
async def get_current_user(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    if not verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"username": user.username, "id": user.id, "email": user.email})
    return Token(access_token=access_token, token_type="bearer")