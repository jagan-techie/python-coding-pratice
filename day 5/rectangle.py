r = 5
c = 15
for i in range(r):
    for j in range(c):
        if i==0 or i==r-1 or j==0 or j==c-1:
            print("*",end="")
        else:
            print(" ",end="")
        if j!= c-1:
            print(" ",end="")
    print()