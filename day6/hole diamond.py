r = 5
for i in range(r):
    for j in range(r-1-i):
        print(" ",end="")
    for j in range(i*2+1):
        if j ==0 or j == i*2 :
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(r-2,-1,-1):
    for j in range(r-1-i):
        print(" ",end="")
    for j in range(i*2+1):
        if j ==0 or j == i*2 :
            print("*",end="")
        else:
            print(" ",end="")
    print()
        