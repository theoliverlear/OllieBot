import sys
import traceback


class OverlappingPinException(Exception):
    def __init__(self, pin_number: int):
        message: str = f"Pin number {pin_number} is already in use."
        super().__init__(message)
        print(message)
        traceback.print_exc()
        sys.exit(1)