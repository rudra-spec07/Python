while True:
    operation = input("Enter operation (+, -, *, /) or 'exit' to quit: ")
    if operation == "exit":
        break
    elif operation in ["+", "-", "*", "/"]:
        try:
            a = int(input("Enter First Number: "))
            b = int(input("Enter Second Number: "))
            match operation:
                case "+":
                    print(f"Addition: {a+b}")
                case "-":
                    print(f"Subtraction: {a-b}")
                case "*":
                    print(f"Multiplication: {a*b}")
                case "/":
                    if b != 0:
                        print(f"Division: {a/b}")
                    else:
                        print("Error: Division by zero is not allowed.")
        except ValueError:
            print("Invalid input. Please enter numbers.")
    else:
        print("Invalid operation. Please enter +, -, *, / or 'exit'.")

print("Calculator has been closed.")    