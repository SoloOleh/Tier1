import turtle
import math

def draw_pythagoras_tree(t, side_length, level):
    if level == 0:
        t.color('green')
        t.begin_fill()
        for _ in range(4):
            t.forward(side_length)
            t.right(90)
        t.end_fill()
        return

    # Draw the base square
    t.forward(side_length)
    t.right(90)
    t.forward(side_length)
    t.right(90)
    t.forward(side_length)

    # Move to the position to start the right branch
    t.right(90)
    t.forward(side_length)
    t.right(45)

    # Draw right branch
    new_side = side_length / math.sqrt(2)
    draw_pythagoras_tree(t, new_side, level-1)

    # Move to the position to start the left branch
    t.left(90)
    t.forward(new_side)
    t.left(90)

    # Draw left branch
    draw_pythagoras_tree(t, new_side, level-1)

    # Return to original position and angle
    t.right(135)
    t.forward(side_length)
    t.left(45)
    t.penup()
    t.backward(side_length)
    t.pendown()
    t.left(90)

def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    t = turtle.Turtle()
    t.speed('fastest')
    t.penup()
    t.goto(-100, -300)
    t.pendown()

    recursion_level = int(input("Enter the recursion level (e.g., 0-10): "))
    draw_pythagoras_tree(t, 100, recursion_level)
    turtle.done()

if __name__ == "__main__":
    main()
