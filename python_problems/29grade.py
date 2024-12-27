def main():
    mark = int(input("Enter your mark: "))
    
    if mark >= 90:
        print("A+ Grade.")
    elif mark >= 80:
        print("A Grade.")
    elif mark >= 70:
        print("B Grade.")
    elif mark >= 60:
        print("C Grade.")
    else:
        print("Sorry. Failed.")

main()