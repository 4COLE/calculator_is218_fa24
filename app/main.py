import sys
from app.calculator import Calculator

def repl():
    calculator = Calculator()
    print("Simple Calculator. Type 'exit' to quit.")

    while True:
        try:
            user_input = input("Enter two numbers and an operation (e.g., '1 2 add'): ")
            if user_input.lower() == 'exit':
                break
            elif user_input.lower() == 'history':
                print(calculator.get_history())
                continue

            a_str, b_str, operation = user_input.split()
            a = float(a_str)
            b = float(b_str)

            result = calculator.perform_calculation(a, b, operation)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    repl()
