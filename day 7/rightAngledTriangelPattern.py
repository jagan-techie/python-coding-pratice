# right angled triangle pattern


# n = 6
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end="")
#     print()
    
# n = 5
# for i in range(1,n+1):
#     for j in range(n+1-i):
#         print("*",end="")
#     print()


#right triangle
r = 10
for i in range(r):
    for j in range(i,r):
        print(" ",end="")
    for k in range(i+1):
        print("*",end="")
    print()
