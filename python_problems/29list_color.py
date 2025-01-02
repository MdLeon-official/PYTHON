def main() :
    lst=[];
    while True:
        color = input("Enter color: (end to terminate): ")
        lst.append(color)
        if color.lower() == "end":
            lst.remove("end")
            print(f"The list of color is {lst} and the total color in this list is {len(lst)}")
            return False


main()
