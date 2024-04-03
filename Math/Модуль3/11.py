import numpy as np

def calculate_vectors_components(vectors):
    """
    Функція для визначення компонент декількох векторів.

    Параметри:
    - vectors: Список кортежів (start_point, end_point), де start_point та end_point - це координати початкової та кінцевої точок вектора.

    Повертає:
    - components: Список кортежів (x_components, y_components), де x_components та y_components - це компоненти по X та Y для кожного вектора.
    """
    components = []

    for start_point, end_point in vectors:
        x_component = end_point[0] - start_point[0]
        y_component = end_point[1] - start_point[1]
        components.append((x_component, y_component))

    return components

# Приклад використання функції з декількома векторами
vectors = [((1, 2), (4, 6)), ((2, 3), (5, 2)), ((0, 0), (-2, 4))]

vector_components = calculate_vectors_components(vectors)
print(vector_components)