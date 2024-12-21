
def main() :
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))

    find_maximum(num1,num2)

def find_maximum(num1, num2):
    if num1 > num2:
        print("Number 1 is bigger.")
    else:
        print("Number 2 is bigger")

main()
