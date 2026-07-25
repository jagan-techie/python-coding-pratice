# Floyd's Triangle

n = 5
sum = 1
for i in range(n):
    for j in range(i):
        print(sum,end=" ")
        sum += 1
    print()
