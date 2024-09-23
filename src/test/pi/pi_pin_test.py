import unittest

from src.main.pi.pi_pin import PiPin
from src.main.pi.pin_state import PinState


class PiPinTest(unittest.TestCase):

    def test_pi_pin_state(self):
        pi_pin = PiPin(1)
        pin_expected_state: PinState = PinState.DISABLED
        self.assertEqual(pi_pin.pin_state, pin_expected_state)

if __name__ == '__main__':
    unittest.main()
