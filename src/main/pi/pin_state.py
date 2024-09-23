from enum import Enum


class PinState(Enum):
    DISABLED = GPIO.LOW
    ENABLED = GPIO.HIGH
