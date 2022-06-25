import asyncio
import functools
import json
import os
from typing import Any, Awaitable, Callable, Dict

from loguru import logger
from pika import URLParameters
from pika.adapters.asyncio_connection import AsyncioConnection
from pika.exchange_type import ExchangeType

from src.infrastructure.rabbitmq.queue_params import QueueParams
from src.infrastructure.rabbitmq.types import (
    ConsumingParserReturnType,
    PublishingParserReturnType,
)

from .config import Settings


class RabbitMQ:

    # A method of getting current rabbit mq instance connection
    _get_connection: Callable[[], AsyncioConnection]

    """The consumers received at least two parameters
        routing_key (str): The routing key for given message
        body (any): The body for given message
    """
    _consumers: set[Callable[[str, any], Awaitable[None]]]

    _consuming_parser: Callable[[PublishingParserReturnType], ConsumingParserReturnType]
    _publishing_parser: Callable[[any], PublishingParserReturnType]

    _queue_prefix: str
    _queue_params: QueueParams

    _settings: Settings

    def __init__(
        self,
        queue_prefix: str = "",
        consuming_parser: Callable[
            [PublishingParserReturnType], ConsumingParserReturnType
        ] = json.loads,
        publishing_parser: Callable[[any], PublishingParserReturnType] = json.dumps,
        queue_params: QueueParams | None = None,
        development: bool = False,
        should_init_app: bool = False,
    ):
        """Initializes a Rabbit MQ instance

        Args:
            queue_prefix (str, optional): Prefix used when naming queues. Defaults to an empty string.
            consuming_parser (Callable[[PublishingParserReturnType], ConsumingParserReturnType] | None, optional):
                Converts received body message using given callable. Defaults to json.loads.
            publishing_parser (Callable[[any], PublishingParserReturnType] | None, optional):
                Converts sending body message using given callable. Defaults to json.dumps.
            queue_params (QueueParams | None, optional): Default parameters for created queues. Defaults to None.
            development (bool, optional): If the is running in development mode. Defaults to False.
            should_init_app (bool, optional): If init_app should be called automatically. Defaults to False
        """

        # TODO: test

        self._consumers = set()
        self._settings = Settings()

        if should_init_app:
            self.init_app(
                queue_prefix=queue_prefix,
                consuming_parser=consuming_parser,
                publishing_parser=publishing_parser,
                queue_params=queue_params,
                development=development,
            )

    async def init_app(
        self,
        queue_prefix: str = "",
        consuming_parser: Callable[
            [PublishingParserReturnType], ConsumingParserReturnType
        ] = json.loads,
        publishing_parser: Callable[[any], PublishingParserReturnType] = json.dumps,
        queue_params: QueueParams | None = None,
        development: bool = False,
    ):
        """Validate connection and sets up consumers

        Args:
            queue_prefix (str, optional): Prefix used when naming queues. Defaults to an empty string.
            consuming_parser (Callable[[PublishingParserReturnType], ConsumingParserReturnType] | None, optional):
                Converts received body message using given callable. Defaults to json.loads.
            publishing_parser (Callable[[any], PublishingParserReturnType] | None, optional):
                Converts sending body message using given callable. Defaults to json.dumps.
            queue_params (QueueParams | None, optional): Default parameters for created queues. Defaults to None.
            development (bool, optional): If the is running in development mode. Defaults to False.
        """

        # TODO: test

        self._consuming_parser = consuming_parser
        self._publishing_parser = publishing_parser
        self._queue_prefix = queue_prefix
        self._queue_params = queue_params or QueueParams()

        self._get_connection = lambda: AsyncioConnection(
            URLParameters(self._settings.mq_url)
        )

        await self._validate_connection()

    async def _validate_connection(self):
        """Validates current connection"""

        try:
            connection = self._get_connection()
            asyncio.Future.


#     def connect(self):
#         logger.info("Connecting to %s", self._url)
#         return AsyncioConnection(
#             pika.URLParameters(self._url),
#             on_open_callback=self.on_connection_open,
#             on_open_error_callback=self.on_connection_open_error,
#             on_close_callback=self.on_connection_closed,
#         )

#     def on_connection_open(self, connection):
#         logger.info("Connection opened")
#         self._connection = connection
#         logger.info("Creating a new channel")
#         self._connection.channel(on_open_callback=self.on_channel_open)

#     def on_connection_open_error(self, _unused_connection, err):
#         logger.error("Connection open failed: %s", err)

#     def on_connection_closed(self, _unused_connection, reason):
#         logger.warning("Connection closed: %s", reason)
#         self._channel = None

#     def on_channel_open(self, channel):
#         logger.info("Channel opened")
#         self._channel = channel
#         self.add_on_channel_close_callback()
#         self.setup_exchange(self.EXCHANGE)

#     def add_on_channel_close_callback(self):
#         logger.info("Adding channel close callback")
#         self._channel.add_on_close_callback(self.on_channel_closed)

#     def on_channel_closed(self, channel, reason):
#         logger.warning("Channel %i was closed: %s", channel, reason)
#         self._channel = None
#         if not self._stopping:
#             self._connection.close()

#     def setup_exchange(self, exchange_name):
#         logger.info("Declaring exchange %s", exchange_name)
#         # Note: using functools.partial is not required, it is demonstrating
#         # how arbitrary data can be passed to the callback when it is called
#         cb = functools.partial(self.on_exchange_declareok, userdata=exchange_name)
#         self._channel.exchange_declare(
#             exchange=exchange_name, exchange_type=self.EXCHANGE_TYPE, callback=cb
#         )

#     def on_exchange_declareok(self, _unused_frame, userdata):
#         logger.info("Exchange declared: %s", userdata)
#         self.setup_queue(self.QUEUE)

#     def setup_queue(self, queue_name):
#         logger.info("Declaring queue %s", queue_name)
#         self._channel.queue_declare(queue=queue_name, callback=self.on_queue_declareok)

#     def on_queue_declareok(self, _unused_frame):
#         logger.info(
#             "Binding %s to %s with %s", self.EXCHANGE, self.QUEUE, self.ROUTING_KEY
#         )
#         self._channel.queue_bind(
#             self.QUEUE,
#             self.EXCHANGE,
#             routing_key=self.ROUTING_KEY,
#             callback=self.on_bindok,
#         )

#     def on_bindok(self, _unused_frame):
#         logger.info("Queue bound")
#         self.start_publishing()

#     def start_publishing(self):
#         logger.info("Issuing Confirm.Select RPC command")
#         self._channel.confirm_delivery(self.on_delivery_confirmation)

#     def on_delivery_confirmation(self, method_frame):
#         confirmation_type = method_frame.method.NAME.split(".")[1].lower()
#         logger.info(
#             "Received %s for delivery tag: %i",
#             confirmation_type,
#             method_frame.method.delivery_tag,
#         )
#         if confirmation_type == "ack":
#             self._acked += 1
#         elif confirmation_type == "nack":
#             self._nacked += 1
#         self._deliveries.remove(method_frame.method.delivery_tag)
#         logger.info(
#             "Published %i messages, %i have yet to be confirmed, "
#             "%i were acked and %i were nacked",
#             self._message_number,
#             len(self._deliveries),
#             self._acked,
#             self._nacked,
#         )

#     def publish_message(self, message):
#         if self._channel is None or not self._channel.is_open:
#             return

#         hdrs = {"a": "b"}
#         properties = pika.BasicProperties(
#             app_id="example-publisher", content_type="application/json", headers=hdrs
#         )

#         self._channel.basic_publish(
#             self.EXCHANGE,
#             self.ROUTING_KEY,
#             json.dumps(message, ensure_ascii=False),
#             properties,
#         )
#         self._message_number += 1
#         self._deliveries.append(self._message_number)
#         logger.info("Published message # %i", self._message_number)


# app = FastAPI()
# ep = None


# @app.on_event("startup")
# async def startup() -> None:
#     global ep
#     await asyncio.sleep(10)  # Wait for MQ
#     user = os.environ["RABBITMQ_DEFAULT_USER"]
#     passwd = os.environ["RABBITMQ_DEFAULT_PASS"]
#     host = os.environ["RABBITMQ_HOST"]
#     port = os.environ["RABBITMQ_PORT"]

#     ep = AsyncioRabbitMQ(f"amqp://{user}:{passwd}@{host}:{port}/%2F")
#     ep.connect()


# JSONObject = Dict[str, Any]


# @app.post("/webhook")
# async def webhook_endpoint(msg: JSONObject) -> None:
#     global ep
#     ep.publish_message(msg)
#     return Response(status_code=204)

# Reference
# https://github.com/pika/pika/blob/main/examples/asyncio_consumer_example.py
