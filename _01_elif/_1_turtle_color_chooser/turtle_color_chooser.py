import random
import turtle
from tkinter import simpledialog


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # TODO 1) Create a new Turtle

    jack = turtle.Turtle()
    #      2) Make the turtle draw a shape (this will take more than one line
    #         of code)
    for i in range(100):
        jack.forward(100)
        jack.left(90)
        jack.forward(100)
        jack.left(90)
        jack.forward(100)
        jack.left(90)
        jack.forward(100)
    #      3) Set the pen width to 10
        chicken = turtle.pensize(10)
    #      4) Ask the user what color pen they would like to draw with
        pen = simpledialog.askstring(title=None, prompt="What color pen")
    #      5) Use an if/else statement to set the pen color that the user
    #         requested
        if pen == "Red":
            jack.pencolor('red')
        if pen == "Green":
            jack.pencolor('green')
        if pen == "Purple":
            jack.pencolor('purple')
        if pen == "Orange":
            jack.pencolor('orange')
        elif pen == "Violet":
            jack.pencolor('violet')
        elif pen == "Blue":
            jack.pencolor('blue')
        elif pen == "Yellow":
            jack.pencolor('yellow')
        elif pen == "Pink":
            jack.pencolor('pink')
        elif pen == "Purple":
            jack.pencolor('purple')
        else:
            get_random_color()

    #      6) If the user doesn't enter anything, choose a random color

    #      7) Put a loop around your code so that you keep asking the user for
    #         more colors & drawing them

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
