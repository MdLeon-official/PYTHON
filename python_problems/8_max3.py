a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("First one is the highest")
elif b > a and b > c:
    print("Second one is the highest")
if c > b and c > a:
    print("Third  one is the highest")
