from datetime import datetime, timedelta
from ..config import settings
from jose import jwt, JWTError
from ...schemas.token import TokenData



SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt



def verify_token(token: str, credentials_exception):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        username = str(payload.get("username"))
        id = str(payload.get("id"))
        email = str(payload.get("email"))

        if username is None or id is None:
            raise credentials_exception
        token_data = TokenData(id=id, username=username, email=email)
        return token_data
    except JWTError:
        raise credentials_exception
    
