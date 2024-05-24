import matplotlib.pyplot as plt
import numpy as np

def draw_tree(ax, root_x, root_y, length, angle, depth, max_depth):
    if depth > max_depth:
        return
    
    end_x = root_x + length * np.cos(angle)
    end_y = root_y + length * np.sin(angle)
    
    ax.plot([root_x, end_x], [root_y, end_y], color='brown', lw=2)
    
    new_length = length * 0.7
    
    draw_tree(ax, end_x, end_y, new_length, angle + np.pi / 4, depth + 1, max_depth)
    draw_tree(ax, end_x, end_y, new_length, angle - np.pi / 4, depth + 1, max_depth)

def create_pythagoras_tree(max_depth):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')
    
    draw_tree(ax, 0, 0, 1, np.pi / 2, 1, max_depth)
    
    plt.show()

max_depth = int(input("Вкажіть рівень рекурсії: "))
create_pythagoras_tree(max_depth)
