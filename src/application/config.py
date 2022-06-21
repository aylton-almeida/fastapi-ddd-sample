from enum import Enum

from pydantic import BaseSettings


class AppEnv(str, Enum):
    production = "production"
    development = "development"
    testing = "testing"


class Settings(BaseSettings):
    app_env: AppEnv
    db_server_url: str


settings = Settings()
