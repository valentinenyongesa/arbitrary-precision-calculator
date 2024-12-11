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

    def subtract(self, other):
        """
        Subtracts another ArbitraryPrecisionCalculator instance from the current value.
        Handles subtraction manually by simulating digit-by-digit subtraction.
        """
        if not isinstance(other, ArbitraryPrecisionCalculator):
            other = ArbitraryPrecisionCalculator(other)

        # Manual subtraction logic
        # For simplicity, assume self >= other (negative handling will be done later)
        result = []
        borrow = 0
        self_value = self.value[::-1]
        other_value = other.value[::-1]

        max_len = max(len(self_value), len(other_value))
        self_value = self_value.ljust(max_len, '0')
        other_value = other_value.ljust(max_len, '0')

        for i in range(max_len):
            digit_diff = int(self_value[i]) - int(other_value[i]) - borrow
            if digit_diff < 0:
                digit_diff += 10
                borrow = 1
            else:
                borrow = 0
            result.append(str(digit_diff))

        # Remove leading zeros
        while len(result) > 1 and result[-1] == '0':
            result.pop()

        return ArbitraryPrecisionCalculator(''.join(result[::-1]))

    def multiply(self, other):
        """
        Multiplies the current value with another ArbitraryPrecisionCalculator instance.
        Handles multiplication manually using digit-by-digit simulation.
        """
        if not isinstance(other, ArbitraryPrecisionCalculator):
            other = ArbitraryPrecisionCalculator(other)

        self_value = self.value[::-1]
        other_value = other.value[::-1]

        result = [0] * (len(self_value) + len(other_value))

        for i in range(len(self_value)):
            for j in range(len(other_value)):
                result[i + j] += int(self_value[i]) * int(other_value[j])
                if result[i + j] >= 10:
                    result[i + j + 1] += result[i + j] // 10
                    result[i + j] %= 10

        # Convert result list to string and remove leading zeros
        while len(result) > 1 and result[-1] == 0:
            result.pop()

        return ArbitraryPrecisionCalculator(''.join(map(str, result[::-1])))

    def divide(self, other):
        """
        Divides the current value by another ArbitraryPrecisionCalculator instance.
        Returns the quotient as an ArbitraryPrecisionCalculator instance.
        """
        if not isinstance(other, ArbitraryPrecisionCalculator):
            other = ArbitraryPrecisionCalculator(other)
        divisor = int(other.value)
        if divisor == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        result = int(self.value) // divisor
        return ArbitraryPrecisionCalculator(result)

    def modulo(self, other):
        """
        Computes the modulo of the current value by another ArbitraryPrecisionCalculator instance.
        """
        if not isinstance(other, ArbitraryPrecisionCalculator):
            other = ArbitraryPrecisionCalculator(other)
        divisor = int(other.value)
        if divisor == 0:
            raise ZeroDivisionError("Modulo by zero is not allowed.")
        remainder = int(self.value) % divisor
        return ArbitraryPrecisionCalculator(remainder)

    def exponentiate(self, other):
        """
        Raises the current value to the power of another ArbitraryPrecisionCalculator instance.
        """
        if not isinstance(other, ArbitraryPrecisionCalculator):
            other = ArbitraryPrecisionCalculator(other)
        base = int(self.value)
        exponent = int(other.value)
        result = base ** exponent
        return ArbitraryPrecisionCalculator(result)

    def factorial(self):
        """
        Computes the factorial of the current value.
        """
        number = int(self.value)
        if number < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        result = 1
        for i in range(1, number + 1):
            result *= i
        return ArbitraryPrecisionCalculator(result)
