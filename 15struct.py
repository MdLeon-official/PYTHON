
user_info = {
    "name" : "Leon",
    "address" : "BD",
    "contact" : 1800000000
}
print(f"Before updating, Contact: {user_info}")

con =  input("Enter your updated contact no(ex: 17xxxxxxxx): ")
user_info.update({"contact" : con})
print(f"After updating, Contact: {user_info}")
