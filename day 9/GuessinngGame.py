secret_number = 7

while True:
    guess = int(input("Guess the secret number (1-10): "))
    
    if guess == secret_number:
        print("Correct! You win!")
        break
    else:
        print("Wrong guess, try again.")
