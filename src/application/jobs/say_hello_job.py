from loguru import logger

from src.infrastructure.apscheduler import scheduler


@scheduler.job("interval", id="do_say_hello", seconds=10, max_instances=1)
async def do_say_hello():
    logger.info("Hello from Scheduler Job")
