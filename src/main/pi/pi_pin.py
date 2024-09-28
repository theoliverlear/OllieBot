from src.main.pi.pin_state import PinState


class PiPin:
    def __init__(self, pin_number: int, pin_state: PinState = PinState.DISABLED):
        self._pin_number = pin_number
        self.pin_state = pin_state

    @property
    def pin_number(self):
        return self._pin_number

    def enqueue_state(self, pin_state: PinState):
        pass

    def prime_state(self, pin_state: PinState):
        if self.is_new_state(pin_state):
            self.pin_state = pin_state

    def set_state(self, pin_state: PinState):
        if self.is_new_state(pin_state):
            self.pin_state = pin_state

    def is_new_state(self, pin_state: PinState) -> bool:
        return not self.pin_state == pin_state

    def toggle_state(self):
        if self.pin_state == PinState.ENABLED:
            self.set_state(PinState.DISABLED)
        else:
            self.set_state(PinState.ENABLED)