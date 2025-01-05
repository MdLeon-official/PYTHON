# QUESTION: Write A python program to get 5 color name from the user in list,
# Display that list, Remove first color and then display all the colors to users

lst = []
for _ in range(5):
    user_input = input("Enter color name: ")
    lst.append(user_input)
print(f"Current list: {lst}")
lst.pop(0)
print(f"After removing first item: {lst}")
