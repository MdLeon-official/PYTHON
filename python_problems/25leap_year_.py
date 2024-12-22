import array

def main():
    arr = array.array("i", [])

    for i in range(0, 5):
        year = int(input("Enter year: "))
        arr.append(year)

    for year in arr:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            print(f"{year} is a leap year.")

main()
