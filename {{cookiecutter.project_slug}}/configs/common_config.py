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
    REDIS_HOST: str = ""
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

    # OpenAI
    OPENAI_API_KEY: str = ""
    KW_ANALYZER_OPENAI_KEY: str = ""
    TOOLS_OPENAI_KEY: str = ""
    AGENT_OPENAI_KEY: str = ""
    EMBEDDING_MODEL: str = "text-embedding-ada-002"

    # Output Formatting
    ENABLE_OUTPUT_FORMATTING: Optional[bool] = True
    FINETUNED_OUTPUT_MODEL: Optional[str] = ""

    # Chat
    CONVERSATION_INACTIVE_HOURS: int = 24

    VERBOSE: bool = False

    # LANGSMITH
    LANGCHAIN_TRACING_V2: Optional[str] = ""
    LANGCHAIN_ENDPOINT: Optional[str] = ""
    LANGCHAIN_API_KEY: Optional[str] = ""
    LANGCHAIN_PROJECT: Optional[str] = ""

    # Logger
    GOOGLE_CHAT_LOGGER_WEBHOOK: str = ""

    class Config:
        env_file = "./.env"
        extra = "allow"


class ConfigKeys:
    OPENAI = "openai"
    VECTORSTORE = "vectorstore"
    NUM_RETRIES = "num_retries"
    DELAY = "delay"
    REQUEST_TIMEOUT = "request_timeout"
    STREAMING = "streaming"
    # Vectorstore
    SEARCH_K = "search_k"
    REQUEST_SEARCH_K = "request_search_k"
    SEARCH_TYPE = "search_type"
    MMR_FETCH_K = "mmr_fetch_k"
    LAMBDA_MULT = "lambda_mult"
    SCORE_THRESHOLD = "score_threshold"

    TOP_N = "top_n"
    REQUEST_TOP_N = "request_top_n"


class ConfigINILoader:
    """
    A class for managing and loading configuration settings from an INI file and environment variables.
    """

    def __init__(
        self,
        config_file_path: Optional[str] = "configs.ini",
    ):
        self.chatbot_config_path = (
            os.path.join(BASE_DIR, config_file_path) if config_file_path else None
        )
        self.file_config = self.load_ini_config(self.chatbot_config_path)

    def load_ini_config(self, config_file_path) -> configparser.ConfigParser:
        config_path = os.path.join(config_file_path)
        config_obj = configparser.ConfigParser()
        if not config_obj.read(config_path):
            raise NotFound()
        return config_obj

    def load_config_section(self, section_name: str) -> Dict[str, Any]:
        if not self.file_config:
            raise ValueError("INI file configuration is not loaded")

        section = self.file_config[section_name]
        return {key: self.parse_config_value(section, key) for key in section}

    @staticmethod
    def parse_config_value(section, key: str) -> Any:
        """
        Parses a value from the config section based on the type inferred from the key.
        """
        if key in [
            ConfigKeys.NUM_RETRIES,
            ConfigKeys.DELAY,
            ConfigKeys.REQUEST_TIMEOUT,
            ConfigKeys.MMR_FETCH_K,
            # Search
            ConfigKeys.SEARCH_K,
            ConfigKeys.REQUEST_SEARCH_K,
            ConfigKeys.TOP_N,
            ConfigKeys.REQUEST_TOP_N,
        ]:
            return section.getint(key)
        elif key in [ConfigKeys.LAMBDA_MULT, ConfigKeys.SCORE_THRESHOLD]:
            return section.getfloat(key)
        elif key == ConfigKeys.STREAMING:
            return section.getboolean(key)
        else:
            return section[key]


settings = Config()
templates = Jinja2Templates(directory="templates")
app_configs: dict[str, Any] = {"title": "my_fastapi API"}
