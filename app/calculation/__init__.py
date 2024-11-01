"""
Calculation module: abstract base class for calculator operations.
"""
from abc import ABC, abstractmethod
from typing import Union
from app.operations import addition, modulo, power, subtraction, multiplication, division

class Calculation(ABC):
    """Abstract base class for calculator operations."""
    @abstractmethod
    def calculate(self, a: float, b: float, operation: str) -> Union[float, str]:
        """Abstract method to perform a calculation."""
        pass  # pragma: no cover

class BasicCalculation(Calculation):
    """Concrete class for basic calculations."""
    def calculate(self, a: float, b: float, operation: str) -> Union[float, str]:
        """Perform the operation based on the input and handle errors."""
        if operation == 'add':
            return a + b
        elif operation == 'subtract':
            return a - b
        elif operation == 'multiply':
            return a * b
        elif operation == 'divide':
            return self.division(a, b)
        elif operation == 'modulo':
            return self.modulo(a, b)
        elif operation == 'power':
            return a ** b
        else:
            return "Invalid operation."

    def division(self, a, b):
        if b == 0:
            return "Cannot divide by zero."
        return a / b

    def modulo(self, a, b):
        if b == 0:
            return "Cannot modulo by zero."
        return a % b