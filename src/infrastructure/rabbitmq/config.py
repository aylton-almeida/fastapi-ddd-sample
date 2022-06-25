import os

from dotenv import load_dotenv

load_dotenv()


class EnvironmentNotFound(Exception):
    """Exception for when environment variable is not found"""


class Settings:

    mq_exchange: str
    mq_url: str

    def __init__(self) -> None:

        # TODO: test

        self.mq_exchange: str = os.getenv("MQ_EXCHANGE")
        self.mq_url: str = os.getenv("MQ_URL")

        if not self.mq_exchange:
            raise EnvironmentNotFound("MQ_EXCHANGE variable not found")

        if not self.mq_url:
            raise EnvironmentNotFound("MQ_URL variable not found")
