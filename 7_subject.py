n = int(input("Enter total subject: "))
sum = 0
for _ in range(n):
    marks = int(input("Enter mark: "))
    sum = sum + marks;

print(f"Total marks: {sum}")
print(f"Average: {sum/n}")
print(f"Percentage: {(sum/n):.2f}%")
