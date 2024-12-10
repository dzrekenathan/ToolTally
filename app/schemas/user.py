from datetime import datetime
from enum import Enum
from pydantic import BaseModel, EmailStr


class UserStatus(str, Enum):
    ENABLED = "enabled"
    DISABLED = "disabled"

class UserCreate(BaseModel):
    username: str
    firstname: str
    lastname: str
    email: EmailStr
    password: str
    verified: bool
    status: UserStatus = UserStatus.ENABLED

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    status: UserStatus = UserStatus.ENABLED
    date_created: datetime