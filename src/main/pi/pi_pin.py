from src.main.pi.pin_state import PinState


class PiPin:
    def __init__(self, pin_number: int, pin_state: PinState):
        self._pin_number = pin_number
        self.pin_state = pin_state

    @property
    def pin_number(self):
        return self._pin_number

    def set_state(self, pin_state: PinState):
        if not self.pin_state == pin_state:
            self.pin_state = pin_state
            self.execute_state()

    def execute_state(self):
        GPIO.output(self.pin_number, self.pin_state.value)

    def toggle_state(self):
        if self.pin_state == PinState.ENABLED:
            self.set_state(PinState.DISABLED)
        else:
            self.set_state(PinState.ENABLED)