from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer


from app.core.database import get_db
from app.models import models
from ...schemas.token import TokenData
from .auth_token import verify_token
from sqlalchemy.orm import Session


credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')



def get_user(email: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == email)
    return user.first()
    


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):

    tokenData: TokenData = verify_token(token, credentials_exception)

    # if tokenData.type != "bearer":
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST,
    #         detail="Invalid token type",
    #     )

    user = get_user(email=tokenData.email, db=db)

    if user is None:
        raise credentials_exception

    return user


def authenticate_user(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == email).first()

    if not user:
        raise credentials_exception
    
    if not verify_token(password, user.password):
        raise credentials_exception
    
    return user

def get_current_active_user(current_user: models.User = Depends(get_current_user)):
    if not current_user.verified:
        raise credentials_exception
    return current_user