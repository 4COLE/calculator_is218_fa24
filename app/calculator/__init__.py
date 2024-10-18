from app.calculation import BasicCalculation
from app.historymanager import historymanager

class calculator:
    def __init__(self):
        self.history_manager = historymanager()
        self.basic_calc = BasicCalculation()

    def perform_calculation(self, a, b, operation):
        result = self.basic_calc.calculate(a, b, operation)
        if isinstance(result, (int, float)):
            self.history_manager.add_to_history(operation, a, b, result)
        return result

    def get_history(self):
        return self.history_manager.show_history()
