
#user input validation
while True:
    number = int(input("Enter a positive number: "))
    
    # Condition to exit: stop looping if number is greater than 0
    if number > 0:
        break

print(f"Thank you! You entered: {number}")
