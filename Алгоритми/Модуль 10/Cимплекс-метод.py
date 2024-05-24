import pulp

model = pulp.LpProblem("Model Name", pulp.LpMinimize)  # Мінімізація
# або
model = pulp.LpProblem("Model Name", pulp.LpMaximize)  # Максимізація

x = pulp.LpVariable('x', lowBound=0, cat='Continuous')  # x ≥ 0
y = pulp.LpVariable('y', 3, 7)        # 3 ≤ y ≤ 7

model += 2 * x + 3 * y, "Problem"  # Мінімізувати або максимізувати 2x + 3y

model += x + 2 * y <= 8, "Constraint1"
model += y >= 2, "Constraint2"

model.solve()

pulp.LpStatus[model.status]


import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize Profit", pulp.LpMaximize)

# Визначення змінних
A = pulp.LpVariable('A', lowBound=0, cat='Integer')  # Кількість продукту А
B = pulp.LpVariable('B', lowBound=0, upBound=10, cat='Integer')  # Кількість продукту Б

# Функція цілі (Максимізація прибутку)
model += 50 * A + 40 * B, "Profit"

# Додавання обмежень
model += 5 * A + 2 * B <= 80  # Обмеження для машини №1
model += 3 * A + 2 * B <= 40  # Обмеження для машини №2

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Виробляти продуктів А:", A.varValue)
print("Виробляти продуктів Б:", B.varValue)
