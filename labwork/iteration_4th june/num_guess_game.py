# Number Guessing Game between 1 and 50

import random  # import random module to generate random number

# computer selects a random number between 1 and 50
secret_number = random.randint(1, 50)

attempts = 0  # counter to count number of tries

print("🎮 Welcome to Number Guessing Game!")
print("Guess the number between 1 and 50")

# loop continues until correct guess
while True:
    # take input from user
    guess = int(input("Enter your guess: "))
    
    # increase attempt count
    attempts += 1

    # check if guess is correct
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("🎉 Correct guess!")
        print("You guessed it in", attempts, "attempts.")
        break  # exit loop when correct guess is made
