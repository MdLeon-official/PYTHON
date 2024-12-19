import array as arr

a = arr.array("i", [])
for _ in range(0,5):
    a.append(int(input("Enter a number in this array: ")))
max = a[0]
for j in range(0,5):
    if max < a[j]:
        max = a[j]
print(max)
