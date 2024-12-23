
def main():
    number = int(input("Enter a number to check if its divisible by 5 or 6: "))
    if number % 5 == 0 and number % 6 == 0:
        print(f"{number} is divisible by 5 and 6.")
    else:
        print(f"{number} is not divisible by 5 and 6.")
main()
