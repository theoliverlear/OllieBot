import sys


class OverlappingPinException(Exception):
    def __init__(self, pin_number: int):
        message: str = f"Pin number {pin_number} is already in use."
        super().__init__(message)
        sys.exit(1)