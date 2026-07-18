password = " "
while password!= "secret123":
    password = input("Enter the password: ")
    if password != "secret123":
        print("Acess denied.try again.")
print("Acess granted!")        