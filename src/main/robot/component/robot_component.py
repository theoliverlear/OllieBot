from abc import ABC, abstractmethod

from src.main.pi.pi_pin import PiPin


class RobotComponent(ABC):
    def __init__(self, pi_pin: PiPin):
        self.pi_pin = pi_pin

    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass
