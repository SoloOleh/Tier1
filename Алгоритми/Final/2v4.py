import turtle

def draw_pythagoras_tree(branch_length, angle, level):
    if level == 0:
        return

    turtle.forward(branch_length)
    turtle.left(angle)

    draw_pythagoras_tree(branch_length * 0.6, angle, level - 1)
    
    turtle.right(angle * 2)
    
    draw_pythagoras_tree(branch_length * 0.6, angle, level - 1)
    
    turtle.left(angle)
    turtle.backward(branch_length)

def main():
    # Ініціалізація Turtle
    turtle.speed(100)
    turtle.left(90)
    turtle.up()
    turtle.backward(200)
    turtle.down()

    # Зчитування рівня рекурсії від користувача
    recursion_level = int(input("Введіть рівень рекурсії: "))
    
    # Малювання дерева
    draw_pythagoras_tree(100, 45, recursion_level)

    # Завершення роботи Turtle
    turtle.done()

if __name__ == "__main__":
    main()