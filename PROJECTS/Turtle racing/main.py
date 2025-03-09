# Mar 9, 2025

import turtle
import random
# import time

# constant for turtle screen
WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black', 'gray']


# Total number of racer turtles
def number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers(2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Invalid output. Please enter a number between 2 and 10.")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Invalid output. Please enter a number between 2 and 10.")

# Turtle 2D screen
def turtle_2d_screen():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!!!")

def create_turtles(colors):
    turtles = []
    spacingX = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingX, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]

# Main codes
def main():
    racers = number_of_racers()
    turtle_2d_screen()

    #get unique colors
    random.shuffle(COLORS)
    colors = COLORS[:racers]

    create_turtles(colors)
    winner = race(colors)
    print(f"The winner is {winner}!")



# Entry point
if __name__ == "__main__":
    main()
