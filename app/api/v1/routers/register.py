from typing import Dict
from fastapi import Body, Depends, APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from jwt import ExpiredSignatureError
from app.core.authentication.auth_token import create_access_token, verify_token
from app.core.authentication.email_verification import send_email_verification
from app.core.authentication.hashing import hash_password
from app.core.database import get_db
from app.models import models
from datetime import timedelta
from sqlalchemy.orm import Session
from app.schemas.token import EmailVerificationToken
from app.schemas.user import UserCreate, UserOut
from app.core.authentication.auth_middleware import get_current_active_user, get_current_user, credentials_exception


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


@router.post("/register/verify", response_model=Dict[str, str])
def verify_email(verification_token: EmailVerificationToken, db: Session = Depends(get_db)) -> JSONResponse:

    try:
        try:
            token_data = verify_token(
                verification_token.verification_token, credentials_exception
            )
        except ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Verification token expired",
            )

        if token_data.type != "email_verification":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid token type",
            )
        
        db.query(models.User).filter(models.User.email == token_data.email).update({"verified": True})
        db.commit()

        return JSONResponse({"message": "Account verified successfuly"})
    except Exception as ex:
        
        raise ex
    
@router.post("/register/verify/resend", response_model=UserOut)
def resend_verification(email: str = Body(embed=True), db: Session = Depends(get_db)) -> JSONResponse:
    """Resends email verification"""

    user = db.query(models.User).filter(models.User.email == email).first()

    if user.verified:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Account already verified",
        )

    verification_token = create_access_token(
        {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "type": "email_verification",
        },
        timedelta(hours=1),
    )

    send_email_verification(user.email, verification_token)

    response_message = {
        "message": "Email verification token resent",
        "token_expire": "1 Hour",
        "email": user.email,
    }

    return JSONResponse(response_message, status_code=200)


@router.post("/register/forgot-password", response_model=Dict[str, str])
def forgot_password(email: str = Body(embed=True), db: Session = Depends(get_db)) -> JSONResponse:

    user = db.query(models.User).filter(models.User.email == email).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    verification_token = create_access_token(
        {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "type": "password_reset",
        },
        timedelta(hours=1),
    )

    send_email_verification(user.email, verification_token)

    return {
        "message": "Password reset token sent",
        "token_expire": "1 Hour",    
        "email": user.email
    }


@router.post("/register/reset-password", response_model=Dict[str, str])
def reset_password(token: str = Body(embed=True), password: str = Body(embed=True), db: Session = Depends(get_db)) -> JSONResponse:

    try:
        token_data = verify_token(token, credentials_exception)

        if token_data.type != "password_reset":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid token type",
            )

        db.query(models.User).filter(models.User.email == token_data.email).update({"password": hash_password(password)})
        db.commit()

        return JSONResponse({"message": "Password reset successfuly"})
    except Exception as ex:
        raise ex