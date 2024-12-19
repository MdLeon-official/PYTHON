password = input("Enter password (length should be less than 8): ")

if password.isalnum() and len(password) < 8:
    print("Your password is ok!")
else:
    print("Please enter a valid password containing only letters and less than 8 characters.")
