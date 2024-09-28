
import time

from src.main.pi.pi_pin import PiPin
from src.main.pi.pin_state import PinState
from src.main.robot.component.light.light import Light
from src.main.robot.robot import Robot

class Main:
    def __init__(self, robot):
        self.robot = robot
    @staticmethod
    def main():
        robot: Robot = Robot.default_robot()
        light: Light = Light(PiPin(17, PinState.DISABLED))
        light.on()
        time.sleep(2)
        light.off()

if __name__ == "__main__":
    Main.main()
    print("Done")
# video_recorder = VideoRecorder.create_from_defaults()
    # video_recorder.record()
