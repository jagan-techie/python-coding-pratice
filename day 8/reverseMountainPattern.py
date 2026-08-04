# r = 6
# for i in range(r):
#     for j in range(r-i):
#         print("*",end="")
#     print()
# for i in range(r,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()

# r=6 
# for i in range(r):
#     for j in range(i+1):
#         print("*",end="")
#     print()
# for i in range(r):
#     for j in range(i+1):
#         print("*",end="")
#     print()
        
        
# r = 4
# for i in range(r):
#     for j in range(r-1-i):
#         print(" ",end="")
#     for k in range(i+1):
#         print("* ",end="")
#     print()
    
    
# r = 4
# for i in range(r):
#     for k in range(i):
#         print(" ",end="")
#     for j in range(r-i):
#         print("*",end="")
#     print()

# r = 4
# for i in range(r):       mountain pattern
#     for j in range(r-1-i):
#         print(" ",end="")
#     for k in range(i*2+1):
#         print("*",end="")
#     print()


# r = 4          
# for i in range(r-1,-1,-1):
#     for j in range(r-1-i):
#         print(" ",end="")     reverse mountain pattern
#     for k in range(i*2+1):
#         print("*",end="")
#     print()


# r = 5
# for i in range(r):
#     for j in range(i):  #reverse mountain pattern
#         print(" ",end="")
#     for k in range(2*r-1-2*i):
#         print("*",end="")
#     print()

r = 6
for i in range(r):       
    for j in range(r-1-i):
        print(" ",end="")
    for k in range(i*2+1):
        print("*",end="")
    print()
for i in range(r-2,-1,-1):
    for j in range(r-1-i):
        print(" ",end="")   
    for k in range(i*2+1):
        print("*",end="")
    print()
    
    
# r = 6
# for i in range(r-1,-1,-1):
#     for j in range(r-1-i):
#         print(" ",end="")   
#     for k in range(i*2+1):
#         print("*",end="")
#     print()
# for i in range(1,r):       
#     for j in range(r-1-i):
#         print(" ",end="")
#     for k in range(i*2+1):
#         print("*",end="")
#     print()