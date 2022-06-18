from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.application.controllers import controllers

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

    @app.get(f"{PATH}/ping")
    async def _():
        return "pong"

    return app
