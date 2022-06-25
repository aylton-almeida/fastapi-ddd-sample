from dataclasses import dataclass


@dataclass(frozen=True)
class QueueParams:

    durable: bool = True
    auto_delete: bool = False
    exclusive: bool = False
    has_dead_letter: bool = False
