def sum(n):
    if n==0:
        return 0
    else:
        return n%10 + sum(n//10)
while True:
    try:
        a=int(input("Enter a number to find sum of digits: "))
        print(f"The sum of digits of {a} is {sum(a)}")
        break
    except ValueError:
        print("Invalid input.Please enter an integer.")

