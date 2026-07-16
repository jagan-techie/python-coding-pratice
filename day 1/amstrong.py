n = int(input())

temp = n
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if sum == n:
    print("Armstrong")
else:
    print("Not Armstrong")