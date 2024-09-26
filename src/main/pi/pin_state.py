from enum import Enum

from RPi import GPIO


class PinState(Enum):
    DISABLED = GPIO.LOW
    ENABLED = GPIO.HIGH
