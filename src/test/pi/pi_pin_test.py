import unittest
from time import sleep

from main.pi.pi_pin import PiPin
from main.pi.pin_state import PinState


class PiPinTest(unittest.TestCase):

    def test_pi_pin_state(self):
        pi_pin = PiPin(1)
        pin_expected_state: PinState = PinState.DISABLED
        self.assertEqual(pi_pin.pin_state, pin_expected_state)

    def test_real_pin_state(self):
        pi_pin = PiPin(17)
        pi_pin.set_state(PinState.ENABLED)
        sleep(1)
        pi_pin.set_state(PinState.DISABLED)
        self.assertTrue(True)
if __name__ == '__main__':
    unittest.main()
