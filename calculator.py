# Arbitrary-Precision Integer Calculator
# Implements basic operations (add, subtract, multiply, divide, factorial) manually using strings.

class ArbitraryPrecisionCalculator:
    """
    A class for performing arbitrary-precision integer calculations.
    This class supports initialization with integer or digit string inputs.
    """

    def __init__(self, value):
        """
        Initializes the calculator with a given integer or digit string.
        """
        if isinstance(value, str) and value.isdigit():
            self.value = value  # Store the number as a string if it's a positive number
        elif isinstance(value, str
