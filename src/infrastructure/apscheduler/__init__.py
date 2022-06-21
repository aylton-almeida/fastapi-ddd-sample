from apscheduler.schedulers.asyncio import AsyncIOScheduler
from loguru import logger


class Scheduler:

    __scheduler: AsyncIOScheduler

    def __init__(self):
        self.__scheduler = AsyncIOScheduler()

    def start(self):

        self.__scheduler.start()

        for task in self.__scheduler.get_jobs():
            logger.info(f"Starting Job {task.name}")

    @property
    def job(self):
        return self.__scheduler.scheduled_job


scheduler = Scheduler()
