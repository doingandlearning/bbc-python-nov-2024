# ERR_API_INVALID
# ERR_SOMETHING_WENT_WRONG
# ERR1234


class InvalidInputError(Exception):
    """Raised when an invalid input is provided."""

    def __init__(self, value, message="Invalid input provided"):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.value}"

def process_input(value):
    # if type(value) != int
    if not isinstance(value, int) or value <= 0:
        raise InvalidInputError(value, "Input must be a positive integer")
    print(f"Processing value: {value}")

# Main program
try:
    process_input(-5)  # Test with an invalid value
except InvalidInputError as e:
    print(e)