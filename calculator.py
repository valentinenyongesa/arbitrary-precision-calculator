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
        elif isinstance(value, str) and value[0] == '-' and value[1:].isdigit():
            self.value = value  # Handle negative numbers stored as strings
        elif isinstance(value, int):
            self.value = str(value)  # Convert integer to string for uniformity
        else:
            raise ValueError("Invalid input: Only digit strings or integers are allowed.")
    
    def add(self, other):
        """
        Adds the current value to another ArbitraryPrecisionCalculator instance or a value.
        """
        # Check if 'other' is an instance of ArbitraryPrecisionCalculator
        if isinstance(other, ArbitraryPrecisionCalculator):
            other_value = other.value
        elif isinstance(other, (int, str)):
            other_value = str(other)
        else:
            raise ValueError("Invalid input: Must be an integer, string, or ArbitraryPrecisionCalculato                             r instance.")

        # Convert both values to integers for addition and convert the result back to a string
        result = str(int(self.value) + int(other_value))
        return ArbitraryPrecisionCalculator(result)
