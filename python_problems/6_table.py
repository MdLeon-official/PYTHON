x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))

print(f"Table of {x}: ")
for i in range(1,10):
    print(f"{x} X {i} = {x*i}")

print(f"Table of {y}: ")
for i in range(1,10):
    print(f"{y} X {i} = {y*i}")
