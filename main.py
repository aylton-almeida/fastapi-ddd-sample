import sys

import uvicorn
from loguru import logger

from src.application.app import create_app

# Setup loguru as logger
logger.remove()
logger.add(
    sys.stdout,
    colorize=True,
    format="<green>{level}</green>:     {function}[{line}] - <level>{message}</level>",
)

app = create_app()


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True)

# TODO: remove https://github.com/agronholm/apscheduler/blob/master/examples/schedulers/async_.py
