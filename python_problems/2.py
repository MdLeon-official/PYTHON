
age  = int(input("Enter your age to check: "))

if age >= 18 :
    print("You will be able to participate in voting.")
elif age < 18 :
    print(f"Sorry! You cannot participate in voting, you will be able to participate after {18-age} year.")
