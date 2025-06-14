from turtle import Turtle, Screen
import random

# Initialize Turtle
my_turtle = Turtle()
screen = Screen()

# Setup the Turtle Configuration
my_turtle.shape("classic")
my_turtle.speed("fastest")
my_turtle.pensize(10) # Set the pen size
my_turtle.hideturtle() # Hide the turtle for a cleaner look

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

def is_out_of_screen(degree):
    """Check if the turtle is about to move out of the screen."""
    x, y = my_turtle.position() # Get current position

    # We need to get half due to the turtle's position being at the center of the shape
    screen_width = screen.window_width() // 2 # Half the width of the screen
    screen_height = screen.window_height() // 2 # Half the height of the screen

    next_x, next_y = my_turtle.xcor(), my_turtle.ycor() # Get current coordinates
    if degree == 0:  # Facing right
        next_x += 50
    elif degree == 90:  # Facing up
        next_y += 50 
    elif degree == 180:  # Facing left
        next_x -= 50
    elif degree == 270:  # Facing down
        next_y -= 50

    return not (-screen_width < next_x < screen_width and -screen_height < next_y < screen_height)

def random_walk():
    """Make the turtle perform a random walk."""
    
    while True: 
        degree = random.choice([0,90,180,270]) # Randomly choose a direction
        turtle_color_change() # Change the turtle's color
        
        if is_out_of_screen(degree): # Check if the turtle is going out of the screen
            print(f"Current degree is {degree}. You are going out of screen. move back.")
            degree = (degree + 180) % 360 # Reverse direction if out of screen
            print(f"Changed degree to {degree}")

        my_turtle.seth(degree) # Set the turtle's heading
        my_turtle.forward(20) # Move the turtle forward

random_walk()

screen.exitonclick()