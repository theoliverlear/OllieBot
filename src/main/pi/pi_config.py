from typing import List

from src.main.pi.pi_pin import PiPin
from src.main.pi.pi_pins import PiPins


class PiConfig:
    LIGHT_CONFIG: 'PiConfig'
    MOTOR_CONFIG: 'PiConfig'
    SOUND_CONFIG: 'PiConfig'
    CAMERA_CONFIG: 'PiConfig'
    DEFAULT_CONFIGS: List['PiConfig'] = [LIGHT_CONFIG, MOTOR_CONFIG, SOUND_CONFIG, CAMERA_CONFIG]
    def __init__(self, pi_pins: PiPins):
        self.pi_pins = pi_pins

    @staticmethod
    def create_from_compatible_configs(*pi_configs: 'PiConfig') -> 'PiConfig':
        for pi_config in pi_configs:
            pass
        pass

    @staticmethod
    def create_from_defaults() -> 'PiConfig':
        return PiConfig.create_from_compatible_configs(*PiConfig.DEFAULT_CONFIGS)