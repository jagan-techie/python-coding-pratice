# Problem 4: Roll a Die Simulation (Advanced)
# Scenario: Simulate rolling a six-sided die. The game should automatically roll the die once and keep rolling until a 6 is rolled. 


import random

while True:
    roll = random.randint(1, 6)
    print(f"You rolled a: {roll}")
    
    # Check if the termination condition is met
    if roll == 6:
        print("Found a 6! Stopping the game.")
        break
