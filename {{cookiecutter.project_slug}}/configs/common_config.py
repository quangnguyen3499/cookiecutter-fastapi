import configparser
import os
from typing import Any
from typing import Dict
from typing import Optional

from core.constants import BASE_DIR
from core.enumerate import Environment
from core.exceptions import NotFound
from dotenv import load_dotenv
from fastapi.templating import Jinja2Templates
from pydantic import PostgresDsn
from pydantic import RedisDsn
from pydantic_settings import BaseSettings

load_dotenv()


class Config(BaseSettings):
    # Database
    POSTGRES_HOST: str = "127.0.0.1"
    POSTGRES_PORT: str = "5432"
    POSTGRES_DB: str = "db"
    POSTGRES_USER: str = "user"
    POSTGRES_PASSWORD: str = "password"
    DATABASE_URI: Optional[PostgresDsn] = f"""
        postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}
    """

    # Redis
    REDIS_HOST: str = "127.0.0.1"
    REDIS_PORT: str = "6379"
    REDIS_URL: Optional[RedisDsn] = f"redis://{REDIS_HOST}:{REDIS_PORT}"
    REDIS_TTL: int = 300

    # Celery
    CELERY_BROKER_URL: str = ""

    # Web Application
    CORS_ORIGINS: Optional[str] = ""
    CORS_ORIGINS_REGEX: Optional[str] = None
    CORS_HEADERS: Optional[str] = ""
    ENVIRONMENT: Optional[str] = Environment(Environment.LOCAL)
    SITE_DOMAIN: str = "localhost"

    # JWT
    JWT_ALG: str = "HS256"
    JWT_SECRET: str = ""
    SECURE_COOKIES: bool = False

    # Chat
    CONVERSATION_INACTIVE_HOURS: int = 24

    VERBOSE: bool = False

    # Logger
    GOOGLE_CHAT_LOGGER_WEBHOOK: str = ""

    class Config:
        env_file = "./.env"
        extra = "allow"


settings = Config()
templates = Jinja2Templates(directory="templates")
app_configs: dict[str, Any] = {"title": "my_fastapi API"}
