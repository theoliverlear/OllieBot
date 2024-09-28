from typing import List, Dict, Optional

from src.main.pi.exception.overlapping_pin_exception import \
    OverlappingPinException
from src.main.pi.pi_pin import PiPin


class PiPins:
    GPIO_PINS = [3, 5, 7, 11, 12, 13, 15, 16, 18, 19, 21, 22, 23, 24, 26, 29, 31, 32, 33, 35, 36, 37, 38, 40]
    def __init__(self, pins: List[PiPin]):
        self.pins = pins
        self.detect_overlapping_pins()

    def detect_overlapping_pins(self) -> None:
        pins_dict: dict[int, PiPin] = {}
        for pin in self.pins:
            if pin.pin_number in pins_dict:
                raise OverlappingPinException(pin.pin_number)
            pins_dict[pin.pin_number] = pin

    def get_pin(self, pi_pin: PiPin) -> Optional[PiPin]:
        for pin in self.pins:
            if pin == pi_pin:
                return pin
        return None
    def get_pin_by_pin_number(self, pin_number: int) -> Optional[PiPin]:
        for pin in self.pins:
            if pin.pin_number == pin_number:
                return pin
        return None

    def pin_is_used(self, pin_number: int) -> bool:
        return self.get_pin_by_pin_number(pin_number) is not None


    def set_pin(self, new_pi_pin: PiPin) -> None:
        for pin in self.pins:
            if pin.pin_number == new_pi_pin.pin_number:
                if self.pin_is_used(new_pi_pin.pin_number):
                    raise OverlappingPinException(pin.pin_number)
                else:
                    pin = new_pi_pin
                    return

    def hard_set_pin(self, new_pi_pin: PiPin) -> None:
        for i in range(len(self.pins)):
            if self.pins[i].pin_number == new_pi_pin.pin_number:
                self.pins[i] = new_pi_pin
                return
        self.pins.append(new_pi_pin)
