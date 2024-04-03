import matplotlib.pyplot as plt
import numpy as np

def draw_vectors(vectors, colors=None, title=None):
    """
    Функція для малювання декількох векторів на площині засобами бібліотеки Matplotlib.

    Параметри:
    - vectors: Список кортежів (start_point, end_point), де start_point та end_point - це координати початкової та кінцевої точок вектора.
    - colors: Список кольорів для векторів (за замовчуванням використовується 'blue' для всіх векторів).
    """
    num_vectors = len(vectors)

    if colors is None:
        colors = ['blue'] * num_vectors

    if title is None:
        title = 'Декілька векторів на площині'

    # Створення нового рисунка та вісей
    fig, ax = plt.subplots()

    for i in range(num_vectors):
        start_point, end_point = vectors[i]

        # Визначення вектора та його довжини
        vector = np.array([end_point[0] - start_point[0], end_point[1] - start_point[1]])
        length = np.linalg.norm(vector)

        # Нормалізація вектора
        # normalized_vector = vector / length
        normalized_vector = vector

        # Додавання стрілки до вісей
        ax.arrow(start_point[0], start_point[1], normalized_vector[0], normalized_vector[1],
                 head_width=0.1, head_length=0.1, fc=colors[i], ec=colors[i])

    # Налаштування візуалізації
    ax.set_title(title)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True)

    # Відображення графіку
    plt.show()

# Приклад використання функції з декількома векторами та кольорами
vectors = [((1, 2), (4, 6)), ((2, 3), (5, 2)), ((0, 0), (-2, 4))]
colors = ['green', 'red', 'purple']

draw_vectors(vectors, colors)