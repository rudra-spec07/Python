def pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

while True:
    try:
        b = int(input("Enter a number: "))
        pattern(b)
        break  # Exit the loop on successful input and execution
    except ValueError:
        print("Invalid input. Please enter an integer.")
    
