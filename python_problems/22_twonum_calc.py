def main() :
    num1 = int(input("Enter Number 1: "))
    num2 = int(input("Enter Number 2: "))
    symbol = (input("Enter a valid arithmetic operator: "))

    if (num1 == "" or num2 == ""):
        print("Please enter a valid number.")
    operation(num1, num2, symbol)

def operation(num1, num2, symbol):
    if symbol == "+":
        print(f"{num1} + {num2} = {num1+num2}")
    elif symbol == "-":
        print(f"{num1} - {num2} = {num1-num2}")
    elif symbol == "*":
        print(f"{num1} X {num2} = {num1*num2}")
    elif symbol == "/":
        print(f"{num1} / {num2} = {num1/num2}")
    elif symbol == "%":
        print(f"{num1} % {num2} = {num1%num2}")
    else:
        print("Please provide a valid arithmetic symbol.")

main()
