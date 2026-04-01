class calci:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
    def mod(self,a,b):
        return a%b
while True:
    try:
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))
        break
    except ValueError:
        print("Invalid input. Please enter integers only.")
c=calci()
print("Addition:",c.add(a,b))
print("Subtraction:",c.sub(a,b))
#object introspection
# print(dir(c))