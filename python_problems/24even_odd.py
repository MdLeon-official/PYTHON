
def main():
    number = int(input("Enter a number: "))
    if number % 2 == 0 :
        print(f"{number} is EVEN.")
        print(f"The square of {number} is {pow(number,2)}")
    else:
        print(f"{number} is ODD.")
        print(f"The square of {number} is {pow(number,2)}")

main()
