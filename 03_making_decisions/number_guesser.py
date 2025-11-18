# Number Guesser - Practice with if statements
import random

print("🎯 NUMBER GUESSING GAME 🎯")
print("I'm thinking of a number between 1 and 20!")
print()

# Computer picks a random number
secret_number = random.randint(1, 20)
guess_count = 0
max_guesses = 5

print(f"You have {max_guesses} guesses to find my number!")
print("-" * 40)

# Game loop
while guess_count < max_guesses:
    guess_count += 1
    guess = int(input(f"Guess #{guess_count}: "))

    if guess == secret_number:
        print(f"🎉 AMAZING! You guessed it in {guess_count} tries!")
        break
    elif guess < secret_number:
        print("📈 Too low! Try a higher number.")
    else:  # guess > secret_number
        print("📉 Too high! Try a lower number.")

    # Show remaining guesses
    remaining = max_guesses - guess_count
    if remaining > 0:
        print(f"You have {remaining} {'guess' if remaining == 1 else 'guesses'} left.")
    print()

else:  # This runs when the loop finishes without breaking
    print(f"😔 Game Over! The number was {secret_number}.")
    print("Better luck next time!")

print()
print("Thanks for playing! 🎮")