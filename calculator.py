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
        Adds another ArbitraryPrecisionCalculator instance or integer to the current value.
        Handles the addition manually by simulating digit-by-digit addition.
        """
        if not isinstance(other, ArbitraryPrecisionCalculator):
            other = ArbitraryPrecisionCalculator(other)

        # Manual addition logic
        result = []
        carry = 0
        self_value = self.value[::-1]
        other_value = other.value[::-1]

        max_len = max(len(self_value), len(other_value))
        self_value = self_value.ljust(max_len, '0')
        other_value = other_value.ljust(max_len, '0')

        for i in range(max_len):
            digit_sum = int(self_value[i]) + int(other_value[i]) + carry
            carry = digit_sum // 10
            result.append(str(digit_sum % 10))

        if carry:
            result.append(str(carry))

        return ArbitraryPrecisionCalculator(''.join(result[::-1]))
