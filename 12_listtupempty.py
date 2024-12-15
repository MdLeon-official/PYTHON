#list
list = [];
for _ in range(0, 6):
    num = input ("Add a number: ")
    list.append(num)
print(list)
list.clear()
print(list)

#tuple
list1 = [];
for _ in range(0, 6):
    num = input ("Add a number: ")
    list1.append(num)
tup = tuple(list1) 
print(tup)
tup = ()
print(tup)