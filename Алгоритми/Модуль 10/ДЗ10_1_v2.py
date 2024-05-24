from pulp import LpMaximize, LpProblem, LpVariable, lpSum, PULP_CBC_CMD

# Створюємо модель лінійного програмування
model = LpProblem(name="optimal-production", sense=LpMaximize)

# Змінні рішення
x1 = LpVariable(name="Lemonade", lowBound=0, cat="Integer")  # кількість "Лимонаду"
x2 = LpVariable(name="Fruit_Juice", lowBound=0, cat="Integer")  # кількість "Фруктового соку"

# Функція цілі: максимізувати виробництво "Лимонаду" і "Фруктового соку"
model += lpSum([x1, x2])

# Обмеження за ресурсами
model += (2 * x1 + 1 * x2 <= 100, "Water")  # обмеження води
model += (1 * x1 <= 50, "Sugar")  # обмеження цукру
model += (1 * x1 <= 30, "Lemon_Juice")  # обмеження лимонного соку
model += (2 * x2 <= 40, "Fruit_Puree")  # обмеження фруктового пюре

# Розв'язуємо задачу
status = model.solve(PULP_CBC_CMD(msg=False))

# Вивід результатів
output = {
    "Status": model.status,
    "Lemonade": x1.value(),
    "Fruit_Juice": x2.value(),
    "Total_Production": model.objective.value()
}
output


from scipy.optimize import linprog

# Коефіцієнти для функції цілі (мінімізація від'ємних значень для максимізації)
c = [-1, -1]  # Максимізація загальної кількості вироблених продуктів (Лимонад і Фруктовий сік)

# Коефіцієнти для нерівностей (Ax <= b)
A = [
    [2, 1],  # Вода
    [1, 0],  # Цукор
    [1, 0],  # Лимонний сік
    [0, 2]   # Фруктове пюре
]

b = [100, 50, 30, 40]  # Обмеження ресурсів

# Межі для змінних
x_bounds = [(0, None), (0, None)]  # Обидві змінні мають бути не менше нуля

# Виконання лінійного програмування
result = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')

# Перевірка статусу розв'язку
if result.success:
    lemonade = result.x[0]
    fruit_juice = result.x[1]
    max_production = -result.fun  # Конвертація результату назад до максимізації
    output = {
        "Lemonade (units)": lemonade,
        "Fruit Juice (units)": fruit_juice,
        "Total Production (units)": max_production
    }
else:
    output = "Не вдалося розв'язати задачу: " + result.message

output


import pulp

# Створення задачі лінійного програмування
model = pulp.LpProblem("Optimize_Production", pulp.LpMaximize)

# Змінні для кількості виробленого "Лимонаду" та "Фруктового соку"
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

# Функція цілі: максимізувати загальну кількість продукції
model += lemonade + fruit_juice

# Обмеження ресурсів
# Вода
model += 2 * lemonade + fruit_juice <= 100, "Water"
# Цукор
model += lemonade <= 50, "Sugar"
# Лимонний сік
model += lemonade <= 30, "Lemon_Juice"
# Фруктове пюре
model += 2 * fruit_juice <= 40, "Fruit_Puree"

# Розв'язання задачі
model.solve()

# Виведення результатів
print("Статус:", pulp.LpStatus[model.status])
print("Кількість виробленого лимонаду:", lemonade.varValue)
print("Кількість виробленого фруктового соку:", fruit_juice.varValue)
print("Загальна кількість вироблених продуктів:", pulp.value(model.objective))

