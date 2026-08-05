r = 6
for i in range(r):
    for j in range(r-1-i):
        print(" ",end="")
    for j in range(i+1,0,-1):
        print(j,end="")
    for j in range(2,i+2):
        print(j,end="")
    print()