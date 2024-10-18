class HistoryManager:
    def __init__(self):
        self.history = []

    def add_to_history(self, operation, a, b, result):
        self.history.append(f"{a} {operation} {b} = {result}")

    def undo_last(self):
        if self.history:
            self.history.pop()

    def show_history(self):
        return "\n".join(self.history)