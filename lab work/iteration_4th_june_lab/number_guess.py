import random

# Number Guessing Game
# The program selects a random secret number between 1 and 50.
# The user keeps guessing until they find the secret number.

# Generate the secret number (inclusive range 1..50)
secret = random.randint(1, 50)

# Count how many guesses the user has made
attempts = 0

while True:
    # Prompt the user for a guess. Converting with int() will raise
    # ValueError if the input is not an integer — no validation here.
    guess = int(input("Enter your guess: "))
    attempts += 1

    # Compare the guess with the secret and give feedback
    if guess > secret:
        print("Too High")
    elif guess < secret:
        print("Too Low")
    else:
        # Correct guess: show attempts and exit the loop
        print("Correct Guess")
        print("Total Attempts:", attempts)
        break  # break exits the surrounding while loop