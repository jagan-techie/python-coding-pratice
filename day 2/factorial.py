num = int(input("enter the number: "))
factorial = 1
while num > 1:
    factorial *= num
    num -= 1
print(f"result: {factorial}")
    