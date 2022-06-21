from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.application.config import AppEnv, settings
from src.application.controllers import controllers
from src.application.jobs import *  # pylint: disable=unused-wildcard-import
from src.infrastructure.apscheduler import scheduler

PATH = "/ddd"


def create_app():
    """Creates new Flask App instance

    Returns:
        Flask: Flask app instance
    """

    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )

    # Register all controllers
    for controller in controllers:
        app.include_router(controller.router, prefix=PATH)

    # Start Scheduler if not in testing mode
    if settings.app_env != AppEnv.testing:
        scheduler.start()

    @app.get(f"{PATH}/ping")
    async def _():
        return "pong"

    return app
