import sys
from app.calculator import calculator

def repl():
    calc = calculator()
    print("simple calculator. type 'exit' to quit.")

    while True:
        try:
            user_input = input("enter two numbers and an operation (e.g., '1 2 add'): ")
            if user_input.lower() == 'exit':
                break
            elif user_input.lower() == 'history':
                print(calc.get_history())
                continue

            a_str, b_str, operation = user_input.split()
            a = float(a_str)
            b = float(b_str)

            result = calc.perform_calculation(a, b, operation)
            print(f"result: {result}")
        except ZeroDivisionError as e:
            print(f"error: {e}")
        except ValueError as e:
            print(f"error: {e}")
        except Exception as e:
            print(f"unexpected error: {e}")

if __name__ == "__main__":
    repl()
