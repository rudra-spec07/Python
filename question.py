#W.A.P. to ask the user to enter a number and print the input whether it is negative or positive or zero.
# num=int(input("Enter a number: "))
# if(num<=0 or num>=0):
#     if num>0:
#         print(f"{num} is a Positive Number")
#     elif num<0:
#         print(f"{num} is a Negative Number")
#     else:
#         print("The number is Zero")

#match case problem
# num=int(input("Enter a number between 1 to 7 to get the day: "))
# match num:
#     case 1:
#         print(f"{num} is Monday")
#     case 2:
#         print(f"{num} is Tuesday")
#     case 3:
#         print(f"{num} is Wednesday")
#     case 4:
#         print(f"{num} is Thursday")
#     case 5:
#         print(f"{num} is Friday")
#     case 6:
#         print(f"{num} is Saturday")
#     case 7:
#         print(f"{num} is Sunday")

#password checker
n=int(input("Enter the password: "))
password=99946
while n!=password:
    print("Wrong Password! Try Again.")
    n=int(input("Enter the password: "))
print("Correct Password! Access Granted.")