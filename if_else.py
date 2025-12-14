# if_else.py
user_input = input("Is it raining (True/False): ").strip().lower()
if user_input == "true":
    is_raining = True
elif user_input == "false":
    is_raining = False
else:
    print("Invalid input. Please enter 'True' or 'False'.")
    exit()

if is_raining:
    print("Take an umbrella")
else:
    print("No need to take an umbrella")
#Match case
a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))
operation=input("Enter operation (+, -, *, /): ")
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
    case _:
        print("Invalid operation")