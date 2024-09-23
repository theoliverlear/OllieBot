from src.main.image.video_recorder import VideoRecorder
from src.main.robot.robot import Robot


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
    video_recorder = VideoRecorder.create_from_defaults()
    video_recorder.record()
    robot: Robot = Robot.default_robot()