from enum import Enum

from pydantic import BaseSettings


class AppEnv(str, Enum):
    production = "production"
    development = "development"
    testing = "testing"


class Settings(BaseSettings):
    app_env: AppEnv

    # Postgres
    db_server_url: str

    # Rabbit MQ
    mq_exchange: str
    mq_url: str


settings = Settings()
