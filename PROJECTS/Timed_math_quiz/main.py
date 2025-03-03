import random
import time

MIN_NUMBER = 1
MAX_NUMBER = 50

def main_operations():
    operators = ['+', '-', '*']
    first_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    second_number = random.randint(MIN_NUMBER, MAX_NUMBER)

    operation = str(first_number) + " " + random.choice(operators) + " " + str(second_number)
    answer = eval(operation)

    return operation, answer


def main():
    input("Press Enter to start the timed math quiz...")
    print("----------------------------------------------")
    try:
        start_time = time.time()
        for i in range(1,11):
            operation, answer = main_operations()
            while True:
                guess = input("Problem #" + str(i) + ": " + operation + " = ")
                if guess == str(answer):
                    break
        end_time = time.time()
        total_time = end_time - start_time
        print(f"Total time taken: {total_time:.2f} seconds")

    except KeyboardInterrupt:
        print("\nKeyboardInterrupt detected. Exiting...")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
