from turtle import Turtle, Screen
import random

# Initialize Turtle
my_turtle = Turtle()
screen = Screen()

# Setup the Turtle Configuration
my_turtle.shape("turtle")
my_turtle.speed("fastest")

def move_top_left():
    """Move the turtle to the top left corner of the screen."""
    my_turtle.penup()
    my_turtle.goto(-screen.window_width() // 2 + 20, screen.window_height() // 2 - 20)
    my_turtle.pendown()

def generate_random_color() -> str:
    """Generate a random hex color."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"#{r:02x}{g:02x}{b:02x}"

def turtle_color_change():
    """Change the turtle's color to a random color."""
    my_turtle.pencolor(generate_random_color())
    my_turtle.fillcolor(generate_random_color())

def turtle_dot_line(steps: int):
    """Draw a line of dots with random colors."""
    for _ in range (steps):
        turtle_color_change()
        my_turtle.dot()
        my_turtle.forward(30)

def wandering_turtle(width: int, height: int):
    """Make the turtle wander."""

    move_top_left() # Start at the top left corner
    my_turtle.penup() # Lift the pen to avoid drawing while moving

    for _ in range (height):

        turtle_dot_line(width)

        if _%2 == 0:
            my_turtle.dot()
            my_turtle.seth(270)  # Set heading to 270 degrees (down)
            my_turtle.forward(30) # Move down 30 units
            my_turtle.seth(180) # Set heading to 180 degrees (left)
        else:
            my_turtle.dot()
            my_turtle.seth(270) # Set heading to 270 degrees (down)
            my_turtle.forward(30) # Move down 30 units
            my_turtle.seth(0) # Set heading to 0 degrees (right)

wandering_turtle(25, 25)

# Close the screen on click
screen.exitonclick()