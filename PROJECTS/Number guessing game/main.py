# Feb 26, 2025


import random

# If user wants to play again
def wanna_play_again():
    print("Do you want to play again? (y/n): ", end="")
    user_input = input().lower();

    if user_input == 'y':
        return True
    elif user_input == 'n':
        return False
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        return wanna_play_again()

# The main code goes here
def main():
    # Hint
    print("Welcome to the Number Guessing Game!")
    print("Guess the number between 0 and 100.")
    print("You have 10 attempts to guess the number.")
    print("Let's begin!")

    # Computer guessed number
    computer_guess = random.randint(0,100)

    count = 0;

    # Main logic
    while True:
        # User guessed number
        user_guess = int(input("Enter your guess: "))
        if user_guess == computer_guess:
            print("Congratulations! You guessed the number!")
            break
        elif user_guess < computer_guess:
            print("You guessed too small!")
        else:
            print("You guessed too high!")

        count += 1
        if count == 10:
            print("You have reached the maximum number of attempts.")
            break
        elif count == 5:
            print("You have reached the halfway point.")

# Entry point of the program
if __name__ == "__main__":
    while True:
        main()
        if not wanna_play_again():
            print("Thanks for playing!")
            break
