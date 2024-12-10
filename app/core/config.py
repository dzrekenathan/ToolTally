from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_username: str
    database_password: str
    database_name: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    reset_password_url: str
    verify_email_url: str
    email_account: str
    email_password: str
    smtp_host: str
    smtp_port: str


    class Config:
        env_file = ".env"



settings = Settings()