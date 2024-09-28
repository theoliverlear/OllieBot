from gpiozero import OutputDevice

from src.main.pi.pi_pin import PiPin
from src.main.pi.pin_state import PinState


class RobotComponent(OutputDevice):
    def __init__(self, pi_pin: PiPin):
        super().__init__(pi_pin.pin_number)
        self.pi_pin = pi_pin

    def on(self):
        self.pi_pin.set_state(PinState.ENABLED)
        self.on()

    def off(self):
        self.pi_pin.set_state(PinState.DISABLED)
        self.off()
