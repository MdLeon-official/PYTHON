
number = int(input("Enter number: "))

for i in range(1,number+1):
    print("*"* i, end="")
    print(" " * (number-i))

print("REVERSE PATTERN")

for i in range(1,number+1):
    print(" " * (number-i), end="")
    print("*"* i)
