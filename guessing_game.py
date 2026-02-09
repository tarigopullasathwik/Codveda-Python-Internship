import random

secret_number = random.randint(1, 100)
max_attempts = 5
attempts = 0

print("\n=== Number Guessing Game ===")
print("I have selected a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess it.\n")

while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
            break

    except ValueError:
        print("Please enter a valid number.")

if attempts == max_attempts and guess != secret_number:
    print(f"\n❌ Game Over! The number was {secret_number}.")
