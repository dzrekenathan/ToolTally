from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from app.core.authentication.auth_token import create_access_token
from app.core.authentication.email_verification import send_email_verification
from app.core.authentication.hashing import hash_password
from app.core.database import get_db
from app.models import models
from datetime import timedelta
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut
from app.core.authentication.auth_middleware import get_current_active_user, get_current_user


router = APIRouter(
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

    verification_token = create_access_token(
        {
            "id": new_user.id,
            "username": new_user.username,
            "email": new_user.email,
            "type": "email_verification",
        },
        timedelta(hours=1),
    )

    send_email_verification(user.email, verification_token)

    response_message = {
            "message": "Account created successfully.\nEmail Verification sent.",
            "token_expire": "1 Hour",
            "email": user.email,
        }


    return JSONResponse(content=response_message, status_code=status.HTTP_201_CREATED)


