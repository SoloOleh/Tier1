import turtle

# Define the recursive function to draw the fractal
def draw_fractal(x, y, length, angle, level):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.setheading(angle)
    turtle.forward(length)

    if level > 0:
        draw_fractal(turtle.xcor(), turtle.ycor(), length * 0.6, angle - 30, level - 1)
        draw_fractal(turtle.xcor(), turtle.ycor(), length * 0.6, angle + 30, level - 1)

# Get the recursion level from the user
recursion_level = int(input("Enter the recursion level: "))

# Set up the turtle screen and initial parameters
turtle.speed(0)
turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()

# Call the recursive function to draw the fractal
draw_fractal(turtle.xcor(), turtle.ycor(), 200, 90, recursion_level)

# Keep the window open until closed
turtle.done()