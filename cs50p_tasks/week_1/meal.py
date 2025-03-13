def main():
    time = input("What time is it? ")
    if time == "":
        print("Invalid input")
    else:
        meal_time = convert(time)
        if 7 <= meal_time <= 8:
            print("breakfast time")
        elif 12 <= meal_time <= 13:
            print("lunch time")
        elif 18 <= meal_time <= 19:
            print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    decimal_time = hours + (minutes / 60)
    return decimal_time


if __name__ == "__main__":
    main()
