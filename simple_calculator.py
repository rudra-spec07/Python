a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))
operation=input("Enter operation (+, -, *, /): ")
print("To end stop the calculator please enter any invalid operation")
while (operation in ['+','-','*','/']):
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
    a=int(input("Enter First Number: "))
    b=int(input("Enter Second Number: "))
    operation=input("Enter operation (+, -, *, /): ")
print("Calculator has been closed.")    