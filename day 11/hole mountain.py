# Hole Mountain
r = 10
for i in range(r):
    for j in range(r-1-i):
        print(" ",end="")
    for j in range(i*2+1):
        if j == i*2 or j == 0 or i == r-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()