# Feb 27, 2025


import random

def main():
    wanna_play = True

    print("Welcome to the Dice Rolling Game!")

    while wanna_play:
        print("Roll the dice? (y/n): ", end="")

        user_choice = input()

        if user_choice.lower() == "y":
            dice_1 = random.randint(1,6)
            dice_2 = random.randint(1,6)
            print(f"You rolled {dice_1} and {dice_2}.")
        elif user_choice.lower() == "n":
            print("Thank you for playing!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            continue



if __name__ == "__main__":
    main()

