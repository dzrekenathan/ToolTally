from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: str
    email: str
    username: str
    type: str


class EmailVerificationToken(BaseModel):
    verification_token: str