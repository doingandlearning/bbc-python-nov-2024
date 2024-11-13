# Set a secret number (e.g., secret_number = 7).
# Use a while loop to keep asking the user for a guess until they get it right.
# If the user guesses correctly, print “Congratulations! You guessed it!” and exit the loop.
# If they guess incorrectly, prompt them to try again.
import random

secret_number = random.randint(1,10)

while True:
    guess = int(input("Guess the secret number: "))
    if guess == secret_number:
        print("Well done! You got it right!")
        break
    else:
        print("Not quite, try again.")

guess = None
while guess != secret_number:
    guess = int(input("Guess the secret number: "))
    if guess == secret_number:
        print("Well done! You got it right!")
    else:
        print("Not quite, try again.")

print("Game over!")