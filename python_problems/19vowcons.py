check = input("Enter a alpha character: ")

if check.isalpha():
    for char in check:
        if char.lower() in ['a','e','i','o','u']:
            print(f"{char} is a VOWEL.")
        else:
            print(f"{char} is a CONSTANT.")
elif check == "":
    print("Please enter something.")
else:
    print("It is a number.")
