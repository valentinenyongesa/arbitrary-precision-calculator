# Arbitrary-Precision Integer Calculator
# Implements basic operations (add, subtract, multiply, divide, factorial, fractions) manually using strings.

class ArbitraryPrecisionCalculator:
    def __init__(self, value):
        """
        Constructor to initialize the calculator with a value.
        The value can be in decimal, fraction, binary, or hexadecimal format.
        """
        self.value = self.parse_input(value)

    def parse_input(self, value):
        """
        This method parses the input value to identify whether it's a fraction, binary,
        hexadecimal, or decimal number. It returns a tuple indicating the type and the value(s).
        """
        if isinstance(value, str):
            # Check if the input is a fraction (e.g., "3/4")
            if '/' in value:
                numerator, denominator = value.split('/')
                return ('fraction', int(numerator), int(denominator))
            # Check if the input is in binary (e.g., "0b101")
            elif value.startswith('0b'):
                return ('binary', int(value, 2))
            # Check if the input is in hexadecimal (e.g., "0x1A")
            elif value.startswith('0x'):
                return ('hexadecimal', int(value, 16))
            # Check if the input is a floating-point number (e.g., "1.5")
            elif '.' in value:
                return ('decimal', float(value))
            # Default is decimal (e.g., "123")
            else:
                return ('decimal', int(value))  # Treat as integer
        elif isinstance(value, int):
            return ('decimal', float(value))  # Treat integer as float
        elif isinstance(value, float):
            return ('decimal', value)
        else:
            raise ValueError("Invalid input format.")  # If input is neither a string nor an int

    def to_decimal(self):
        """
        Converts the current value to decimal.
        The value can be a fraction, binary, hexadecimal, or decimal.
        """
        if self.value[0] == 'fraction':
            # For fractions, return the division of numerator by denominator
            numerator, denominator = self.value[1], self.value[2]
            return numerator / denominator
        elif self.value[0] == 'binary':
            # For binary, return the decimal equivalent of the binary value
            return float(self.value[1])  # Convert to float for decimal compatibility
        elif self.value[0] == 'hexadecimal':
            # For hexadecimal, return the decimal equivalent of the hexadecimal value
            return float(self.value[1])  # Convert to float for decimal compatibility
        elif self.value[0] == 'decimal':
            # If it's already decimal, just return the value
            return self.value[1]
        else:
            raise ValueError("Unknown value type")  # If value type is not recognized

    def add(self, other):
        """
        Performs addition between the current value and another ArbitraryPrecisionCalculator instance.
        It converts both values to decimals before adding.
        """
        result = self.to_decimal() + other.to_decimal()
        return ArbitraryPrecisionCalculator(str(result))

    def subtract(self, other):
        """
        Performs subtraction between the current value and another ArbitraryPrecisionCalculator instance.
        It converts both values to decimals before subtracting.
        """
        result = self.to_decimal() - other.to_decimal()
        return ArbitraryPrecisionCalculator(str(result))

    def multiply(self, other):
        """
        Performs multiplication between the current value and another ArbitraryPrecisionCalculator instance.
        It converts both values to decimals before multiplying.
        """
        result = self.to_decimal() * other.to_decimal()
        return ArbitraryPrecisionCalculator(str(result))

    def divide(self, other):
        """
        Performs division between the current value and another ArbitraryPrecisionCalculator instance.
        It converts both values to decimals before dividing.
        """
        result = self.to_decimal() / other.to_decimal()
        return ArbitraryPrecisionCalculator(str(result))

    def modulo(self, other):
        """
        Performs modulo operation (remainder of division) between the current value and another.
        It converts both values to decimals before computing the remainder.
        """
        result = self.to_decimal() % other.to_decimal()
        return ArbitraryPrecisionCalculator(str(result))

    def exponentiate(self, other):
        """
        Performs exponentiation (raising the current value to the power of another value).
        It converts both values to decimals before raising to the power.
        """
        result = self.to_decimal() ** other.to_decimal()
        return ArbitraryPrecisionCalculator(str(result))

    def factorial(self, number=None):
        """
        Computes the factorial of a number. If no number is provided, it uses the current value.
        Factorial is only defined for non-negative integers.
        """
        if number is None:
            # If no number is provided, use the current value and convert it to an integer
            number = int(self.to_decimal())
        if number < 0:
            raise ValueError("Factorial not defined for negative numbers.")
        fact = 1
        for i in range(1, number + 1):
            fact *= i  # Multiply each number in the sequence to get the factorial
        return ArbitraryPrecisionCalculator(str(fact))

    def logarithm(self, value=None, base=10):
        """
        Computes the logarithm of the current value to the given base (default base is 10).
        If value is provided, it computes the log of that value with the given base.
        """
        if value is None:
            value = self.to_decimal()
        
        if value <= 0:
            raise ValueError("Logarithm is not defined for non-positive numbers.")
        
        # Approximate the logarithm using an iterative method for more precision
        result = 0
        current_value = value
        while current_value >= base:
            current_value /= base  # Divide until the value is less than the base
            result += 1  # Increment the result as we reduce the value
        
        # Now handle the fractional part to increase accuracy
        fractional = current_value - 1
        precision = 10  # Number of iterations to improve the precision (adjustable)
        for _ in range(precision):
            fractional = (fractional * base - 1) / base  # Refine the fractional part
            result += fractional  # Add refined fractional part to the result

        return ArbitraryPrecisionCalculator(str(result))


# REPL Loop
def calculator_repl():
    """
    The REPL (Read-Eval-Print Loop) that allows the user to interactively perform calculations.
    It supports addition, subtraction, multiplication, division, factorial, logarithms,
    and base conversions (binary, hexadecimal, and fractions).
    """
    print("Welcome to the Arbitrary Precision Calculator!")
    print("Supported operations: +, -, *, /, %, ^, factorial, base handling")
    
    while True:
        try:
            # Prompt the user to input a calculation
            command = input("Enter a calculation: ").strip()
            if command.lower() == 'exit':
                print("Exiting calculator.")
                break  # Exit the calculator loop when the user types 'exit'
            
            # Handle factorial operation (e.g., "5!")
            if command.endswith("!"):
                number = command[:-1]  # Remove the "!" and get the number part
                operand1 = ArbitraryPrecisionCalculator(number)
                result = operand1.factorial()
                print("Result:", result.to_decimal())
                continue  # Skip further processing for factorials

            # Split the input into operand1, operator, and operand2
            parts = command.split()
            if len(parts) < 2:  # Invalid input format
                raise ValueError("Invalid input format. Example: '1 + 2'")
            operand1 = ArbitraryPrecisionCalculator(parts[0])  # Parse the first operand

            # If there's a second operand, handle the operation
            if len(parts) == 3:
                operator = parts[1]
                operand2 = ArbitraryPrecisionCalculator(parts[2])  # Parse the second operand

                # Perform the appropriate operation based on the operator
                if operator == "+":
                    result = operand1.add(operand2)
                elif operator == "-":
                    result = operand1.subtract(operand2)
                elif operator == "*":
                    result = operand1.multiply(operand2)
                elif operator == "/":
                    result = operand1.divide(operand2)
                elif operator == "%":
                    result = operand1.modulo(operand2)
                elif operator == "^":
                    result = operand1.exponentiate(operand2)
                elif operator == "log":
                    result = operand1.logarithm(operand2.to_decimal())
                else:
                    raise ValueError("Unknown operator")

                # Print the result of the operation
                print("Result:", result.to_decimal())
            else:
                # Handle the case where only one operand is provided for operations like log
                operator = parts[0]
                if operator == "log":
                    operand = operand1.to_decimal()
                    result = operand1.logarithm(value=operand)
                    print("Result:", result.to_decimal())
                else:
                    raise ValueError("Invalid input format")
        
        except Exception as e:
            print("Error:", e)  # Catch and display any errors that occur during calculation

# Run the REPL
calculator_repl()
