# Feb 25, 2025


import random

# Declaring this if user wants to play again
wanna_play = True


# To split the secret number into an array of digits
def split_number(random_number_goes_here):
    ran_num_arr = []
    while random_number_goes_here > 0:
        digit = random_number_goes_here % 10
        ran_num_arr.append(digit)
        random_number_goes_here //= 10
    ran_num_arr.reverse()
    return ran_num_arr


# Give user clues to find the secret number
def get_clues(user_guess, cmp_generated):
    clues = []
    for i in range(0,3):
        if user_guess[i] == cmp_generated[i]:
            clues.append("Fermi")
        elif user_guess[i] in cmp_generated:
            clues.append("Pico")
    if not clues:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)


# Main function to run the game
def main():
    print("I am thinking of a 3-digit number. Try to guess what it is.")
    print("Here are some clues:")
    print("When I say:    That means:")
    print("  Pico         One digit is correct but in the wrong position.")
    print("  Fermi        One digit is correct and in the right position.")
    print("  Bagels       No digit is correct.")

    random_number = random.randint(100,999)
    cmp_arr = split_number(random_number)

    print("I have thought up a number.")
    print("You have 10 guesses to get it right.")

    for i in range(1,11):
        print(f"Guess #{i}: ")
        print("> ", end="")
        try:
            user_input = int(input())
        except ValueError:
            print("Please enter a number!")
            continue
        user_arr = split_number(user_input)

        if random_number == user_input:
            print("You got it!")
            break

        clues = get_clues(user_arr, cmp_arr)
        print(clues)

        if i == 10:
            print("You ran out of guesses!")
            print(f"The number was {random_number}")

    # Checking if the user wants to play again
    print("Do you want to play again? (yes/no) ")
    play_again = input().lower()
    if play_again == "yes":
        main()
    elif play_again == "no":
        print("Thanks for playing!")

if __name__ == "__main__":
    main()
