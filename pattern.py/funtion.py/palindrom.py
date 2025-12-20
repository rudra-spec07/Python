def pali(n):
    for i in range(1,n+1):
        for j in range(n,i,-1):
            print(" ",end=" ")
        for k in range(1,i+1):
            print(k ,end=" ")
        for l in range(i,0,-1):
            print(l ,end=" ")
        print()

while True:
    try:
        num=int(input("Enter the  number of Rows: "))
        pali(num)
        break
    except ValueError:
        print("Invalid input.Please enter an integer.")