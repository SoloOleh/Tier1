import sympy as sp
from sympy import plot

# Визначимо символи
x = sp.symbols('x')
a = 9  # старт робочого дня
b = 18  # кінець робочого дня

# Визначимо функцію ефективності, використовуючи вираз, наданий користувачем
efficiency_function = 2 * ((4 / (1.2 * sp.sqrt(2 * sp.pi)) * sp.exp(-0.5 * ((x - 11) / 1.2)**2)) +
                     (7 / (2.4 * sp.sqrt(2 * sp.pi)) * sp.exp(-0.5 * ((x - 15) / 2.4)**2)))

#невизначений інтеграл функції
indefinite_integral = sp.integrate(efficiency_function, x)

#інтеграл функції від a до b
definite_integral = sp.integrate(efficiency_function, (x, a, b))

# Візуалізуємо функцію на відрізку від 0 до 24
p = plot(efficiency_function, (x, 0, 24), title="Ефективність роботи від часу доби",
     xlabel='Час доби', ylabel='Ефективність роботи', show=False)
p.xlim = [0, 24]
p.show()

print("невизначений інтеграл функції: {indefinite_integral}") 
print("інтеграл функції від a до b: {definite_integral}")


