#slant star pattern from left to right

r = 10
c = 5
for i in range(r):
    for j in range(i):
        print(" ",end="")
    for k in range(c):
        print("*",end="")
    print()
    