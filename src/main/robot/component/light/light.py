from src.main.robot.component.robot_component import RobotComponent


class Light(RobotComponent):
    def __init__(self, pi_pin):
        super().__init__(pi_pin)