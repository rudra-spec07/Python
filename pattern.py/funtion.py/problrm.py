def rev(n):
    rev_num=0
    while n>0:
        rem=n%10
        rev_num=rev_num*10 + rem
        n=n//10
    print(f"The reverse of the given {n} is {rev_num}")

num=int(input("Enter a number: "))    
rev(num)