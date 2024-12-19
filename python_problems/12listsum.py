# Working with a list
lst = []

for _ in range(0, 6):
    user_input = int(input("Enter number: "))
    lst.append(user_input)

print(lst)
print("Sum of list:", sum(lst))

# Working with a tuple
temp_list = [] 
for _ in range(0, 6):
    tup_input = int(input("Enter number: "))
    temp_list.append(tup_input)

tup = tuple(temp_list)
print(tup)
print("Sum of tuple:", sum(tup))
