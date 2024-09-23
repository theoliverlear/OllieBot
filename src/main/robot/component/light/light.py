from typing import override

from src.main.pi.pin_state import PinState
from src.main.robot.component.robot_component import RobotComponent


class Light(RobotComponent):
    def __init__(self, pi_pin):
        super().__init__(pi_pin)

    @override
    def on(self):
        self.pi_pin.set_state(PinState.ENABLED)

    @override
    def off(self):
        self.pi_pin.set_state(PinState.DISABLED)