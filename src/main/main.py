
import time

from src.main.pi.pi_pin import PiPin
from src.main.pi.pin_state import PinState
from src.main.robot.robot import Robot
import gpiozero
class Main:
    robot: Robot
    def __init__(self, robot):
        self.robot = robot
        pass
    @staticmethod
    def main():
        robot: Robot = Robot.default_robot()
        robot.pi_controller.pi_pins.set_pin(PiPin(11, PinState.DISABLED))
        robot.pi_controller.pi_pins.get_pin_by_pin_number(11).set_state(PinState.ENABLED)
        time.sleep(1)
        robot.pi_controller.pi_pins.get_pin_by_pin_number(11).set_state(PinState.DISABLED)
if __name__ == '__main__':
    Main.main()
    # video_recorder = VideoRecorder.create_from_defaults()
    # video_recorder.record()
