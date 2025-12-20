n=int(input("Enter a number: "))
def fib(a):
    if a<=0:
        return []
    elif a==1:
        return [0]
    elif a==2:
        return [0,1]
    else:
        fib_seq=[0,1]
        for i in range(2,a):
            next_fib=fib_seq[i-1]+fib_seq[i-2]
            fib_seq.append(next_fib)
        return fib_seq
# def fib(n):
#     if(n==0):
#         return 0
#     elif(n==1):
#         return 1
#     else:
#         rev=fib(n-2) + fib(n-1)
#         return rev
print(fib(n))



