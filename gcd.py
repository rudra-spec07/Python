# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# while b != 0:
#     a, b = b, a % b

# print("GCD =", a)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd = 0
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i
        print(gcd,end=", ")

print("GCD of", a, "and", b, "is:", gcd)