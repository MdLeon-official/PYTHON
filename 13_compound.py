inp = int(input("Enter a number: "))
sum = 0
print(f"{inp} += ", end="")
inp= inp + 1
print(f"Answer {inp}")
sum = sum + inp

print(f"{inp} -= ", end="")
inp= inp  - 1
print(f"Answer {inp}")
sum = sum + inp

print(f"{inp} *= ", end="")
inp= inp  * 1
print(f"Answer {inp}")
sum = sum + inp

print(f"{inp} /= ", end="")
inp= inp  / 1
print(f"Answer {inp}")
sum = sum + inp


print(sum)