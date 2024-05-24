import pulp

# Створення проблеми
problem = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні для кількості виробленого Лимонаду та Фруктового соку
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

# Обмеження ресурсів
water = 100
sugar = 50
lemon_juice = 30
fruit_puree = 40

# Додавання обмежень
problem += 2 * lemonade + fruit_juice <= water, "Water"
problem += lemonade <= sugar, "Sugar"
problem += lemonade <= lemon_juice, "Lemon_Juice"
problem += 2 * fruit_juice <= fruit_puree, "Fruit_Puree"

# Функція мети
problem += lemonade + fruit_juice, "Total_Production"

# Розв'язання задачі
problem.solve()

# Виведення результатів
print(f"Status: {pulp.LpStatus[problem.status]}")
print(f"Лимонад: {lemonade.varValue}")
print(f"Фруктовий сік: {fruit_juice.varValue}")
print(f"Загальна кількість вироблених продуктів: {lemonade.varValue + fruit_juice.varValue}")
