#Reverse Mountain Pattern.

r = 6
for i in range(r,-1,-1):
    for j in range(r-i):
        print(" ",end="")    
    for k in range(i*2+1):
        print("*",end="")
    print()