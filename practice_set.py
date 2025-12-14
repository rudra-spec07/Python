#typecasting str to int and 10 
nu="45"
print(int(nu)+10)
#using f string
food= input("enter your favourite food: ")
print(f"Wow ! I also like <{food}>")
#simple calculator 
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
add=a+b
sub=a-b
mul=a*b
div=a/b
floor_div=a//b
print(f"Addition: {add}, Subtraction: {sub}, Multiplication: {mul}, Division: {div}, Floor Division: {floor_div}")
#using escape sequences
print("Rudra Said,\"Python is Awesome!\"\n This is on a new line\nthis is for \t tab")
#operator challenge 
a=int(input("Enter number: "))
print(f"square is {a**2}\ncube is {a**3}")