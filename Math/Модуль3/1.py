import plotly.graph_objects as go
import numpy as np

# Генерація точок
num_points = 10
points_x = np.random.randint(-10, 10, num_points)
points_y = np.zeros(num_points)

# Створення об'єкту "Figure" для графіку
fig = go.Figure()

# Додавання горизонтальної вісі X
fig.add_trace(go.Scatter(x=[-10, 10], y=[0, 0], mode='lines', name='X-axis'))

# Додавання точок на координатну пряму
fig.add_trace(go.Scatter(x=points_x, y=points_y, mode='markers', name='Points'))

# Налаштування вигляду графіку
fig.update_layout(
    title='Координатна пряма з точками',
    xaxis=dict(title='Вісь X'),
    yaxis=dict(title='Вісь Y'),
    showlegend=True
)

# Відображення графіку
fig.show()