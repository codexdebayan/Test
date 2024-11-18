class Calculator:
    print("checking the file")
    print("Added webhook so every commit is checked and working..")
    def add(self, a: int, b: int) -> int:
        """Return the sum of two positive integers."""
        self._validate_positive_integer(a)
        self._validate_positive_integer(b)
        return a + b

    def subtract(self, a: int, b: int) -> int:
        """Return the difference of two positive integers."""
        self._validate_positive_integer(a)
        self._validate_positive_integer(b)
        return a - b

    def multiply(self, a: int, b: int) -> int:
        """Return the product of two positive integers."""
        self._validate_positive_integer(a)
        self._validate_positive_integer(b)
        return a * b

    def _validate_positive_integer(self, value: int):
        """Check if the value is a positive integer."""
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Both numbers must be positive integers")
