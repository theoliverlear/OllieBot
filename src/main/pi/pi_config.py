from typing import List

from src.main.pi.pi_pin import PiPin
from src.main.pi.pi_pins import PiPins


class PiConfig:
    LIGHT_CONFIG: 'PiConfig' = None
    MOTOR_CONFIG: 'PiConfig' = None
    SOUND_CONFIG: 'PiConfig' = None
    CAMERA_CONFIG: 'PiConfig' = None
    DEFAULT_CONFIGS: List['PiConfig'] = [LIGHT_CONFIG, MOTOR_CONFIG, SOUND_CONFIG, CAMERA_CONFIG]
    def __init__(self, pi_pins: PiPins):
        self.pi_pins = pi_pins

    def add_and_overwrite_pins(self, *pi_pins: PiPin) -> None:
        for pin in pi_pins:
            self.pi_pins.set_pin(pin)

    @staticmethod
    def create_from_compatible_configs(*pi_configs: 'PiConfig') -> 'PiConfig':
        pi_pins: PiPins = PiPins([])
        pi_config: PiConfig = PiConfig(pi_pins)
        for config in pi_configs:
            pi_config.add_and_overwrite_pins(*config.pi_pins.pins)
        return pi_config



    @staticmethod
    def create_from_defaults() -> 'PiConfig':
        return PiConfig.create_from_compatible_configs(*PiConfig.DEFAULT_CONFIGS)