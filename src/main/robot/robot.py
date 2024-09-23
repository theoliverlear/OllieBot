from src.main.pi.pi_config import PiConfig
from src.main.pi.pi_controller import PiController
from src.main.robot.component.wheel.wheel_set import WheelSet


class Robot:
    def __init__(self, pi_controller: PiController):
        self.pi_controller = pi_controller


    def start(self):
        pass


    def listen(self):
        pass

    @staticmethod
    def default_robot():
        default_config: PiConfig = PiConfig.create_from_defaults()
        return Robot(PiController(default_config))