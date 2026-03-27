from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Customer Support Agent"
    ENV: str = "development"
    DEBUG: bool = True
    # Database URL placeholder; override via env
    DATABASE_URL: str = "sqlite+aiosqlite:///:memory:"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
