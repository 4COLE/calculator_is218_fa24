from abc import ABC, abstractmethod
from app.operations import addition, subtraction, multiplication, division

class Calculation(ABC):
    @abstractmethod
    def calculate(self, a, b):
        pass

class Addition(Calculation):
    def calculate(self, a, b):
        return addition(a, b)

class Subtraction(Calculation):
    def calculate(self, a, b):
        return subtraction(a, b)

class Multiplication(Calculation):
    def calculate(self, a, b):
        return multiplication(a, b)

class Division(Calculation):
    def calculate(self, a, b):
        return division(a, b)