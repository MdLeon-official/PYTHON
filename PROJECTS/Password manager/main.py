# Mar 1, 2025

main_password = "secret"
input_pass = input("Enter your main password: ")
if input_pass != main_password:
    print("Wrong password!")
    exit()

def view():
    try:
        with open("password.txt", 'r') as file:
            for line in file:
                data = line.rstrip()
                user, passw = data.split(" | ")
                print("User:", user, "| Password:", passw)
    except FileNotFoundError:
        print("No passwords stored yet!")

def add():
    username = input("Name: ")
    user_pass = input("Password: ")
    with open("password.txt", 'a') as file:
        file.write(username + " | " + user_pass + "\n")

def main():
    while True:
        mode = input("Would you like to add a new password or view existing passwords: (view, add), press 'q' to quit? ")
        if mode == "q":
            break
        if mode == "view":
            view()
        elif mode == "add":
            add()
        else:
            print("Invalid mode")

if __name__ == "__main__":
    main()
