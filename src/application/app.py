from fastapi import FastAPI

from src.application.controllers import controllers

PATH = '/ddd'


def create_app():
    """Creates new Flask App instance

    Returns:
        Flask: Flask app instance
    """

    app = FastAPI()

    # Register all controllers
    for controller in controllers:
        app.include_router(
            controller.router, prefix=PATH)

    @app.get(f'{PATH}/ping')
    async def _():
        return 'pong'

    return app
