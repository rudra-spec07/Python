for i in range(1,6):
    for j in range(1,10):
        if(j<=i or j>=10-i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()    
for i in range(1,5):
    for j in range(1,10):
        if(j<=5-i or j>=5+i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()  
