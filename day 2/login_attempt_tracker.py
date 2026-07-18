attempts = 3
while attempts > 0:
    password = input("enter the password: ")
    if password == "jagan@123":
        print("Acess granted!")
        break
    attempts -= 1
    print(f"attempts remaining: {attempts}")
else:
    print("Account locked. ")
    