from src.main.pi.pi_config import PiConfig
from src.main.pi.pi_pin import PiPin
from src.main.pi.pi_pins import PiPins
from src.main.robot.robot import Robot


class PiController:
    def __init__(self, pi_config: PiConfig):
        self.pi_config = pi_config
        self.pi_pins = PiPins(pi_config.pins)

    def apply_config(self):
        pass
