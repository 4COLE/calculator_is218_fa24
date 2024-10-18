from app.calculation import Addition, Subtraction, Multiplication, Division
from app.historymanager import HistoryManager

class Calculator:
    def __init__(self):
        self.history_manager = HistoryManager()
        self.operations = {
            'add': Addition(),
            'subtract': Subtraction(),
            'multiply': Multiplication(),
            'divide': Division()
        }

    def perform_calculation(self, a, b, operation):
        if operation in self.operations:
            result = self.operations[operation].calculate(a, b)
            self.history_manager.add_to_history(operation, a, b, result)
            return result
        else:
            raise ValueError("Invalid operation")

    def get_history(self):
        return self.history_manager.show_history()