from datetime import datetime, timedelta, UTC

from app.schemas.token import TokenData
from ..config import Settings, settings
from jose import jwt, JWTError
from typing import Any, Union


SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes


def create_access_token(data: dict[str, Any], expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()


    if expires_delta is not None:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})
    
    # Debug log
    print(f"Payload to encode: {to_encode}")

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt



def verify_token(token: str, credentials_exception):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        
        id = str(payload.get("id"))
        username = str(payload.get("username"))
        email = str(payload.get("email"))
        token_type: str = payload.get("type")

        if username is None or id is None:
            raise credentials_exception
        token_data = TokenData(id=id, username=username, email=email, type=token_type)
        return token_data
    except JWTError:
        raise credentials_exception
    
