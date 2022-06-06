import secrets

from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str
    APP_HOST: str
    APP_PORT: int
    APP_LOG_LEVEL: str
    ENV: str

    POSTGRES_DATABASE_URI: str

    class Config:
        env_file = '.env'


settings = Settings()
