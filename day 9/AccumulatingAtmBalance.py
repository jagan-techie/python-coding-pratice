balance = 0

while True:
    deposit = float(input("Enter amount to deposit (or 0 to exit): "))
    balance += deposit
    
    # Check if user wants to exit
    if deposit == 0:
        break

print(f"Transaction closed. Your total balance is: ${balance:.2f}")
