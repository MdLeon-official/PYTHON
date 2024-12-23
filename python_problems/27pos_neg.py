def main():
    number = int(input("Enter a number to check if its positive or negative: "))
    if number > 0:
        print(f"{number} is positive.")
    elif number == 0:
        print("Equal to zero(0).")
    else:
        print(f"{number} is negative.")

main()
