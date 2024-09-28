from enum import Enum

from RPi import GPIO


class PinState(Enum):
    DISABLED = 0
    ENABLED = 1
