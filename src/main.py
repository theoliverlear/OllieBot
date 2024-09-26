from main.pi.pi_pin import PiPin
from main.pi.pin_state import PinState
from src.main.image.video_recorder import VideoRecorder
from src.main.robot.robot import Robot
import time

class Main:
    robot: Robot
    def __init__(self, robot):
        self.robot = robot
        pass
    @staticmethod
    def main():
        robot: Robot = Robot()
        robot.start()
if __name__ == '__main__':
    Main.main()
    # video_recorder = VideoRecorder.create_from_defaults()
    # video_recorder.record()
    robot: Robot = Robot.default_robot()
    robot.pi_controller.pi_pins.set_pin(PiPin(11, PinState.DISABLED))
    robot.pi_controller.pi_pins.get_pin_by_pin_number(11).set_state(PinState.ENABLED)
    time.sleep(1)
    robot.pi_controller.pi_pins.get_pin_by_pin_number(11).set_state(PinState.DISABLED)