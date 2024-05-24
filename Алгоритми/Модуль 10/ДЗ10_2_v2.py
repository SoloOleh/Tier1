import numpy as np
import scipy.integrate as spi

# Визначаємо функцію, яку потрібно інтегрувати
def f(x):
    return x**2

# Межі інтегрування
a, b = 0, 2

# Аналітичний розрахунок інтеграла
analytical_integral = (b**3 / 3) - (a**3 / 3)

# Використання quad для обчислення інтеграла
quad_result, quad_error = spi.quad(f, a, b)

# Метод Монте-Карло
n_samples = 100000
x_random = np.random.uniform(a, b, n_samples)
y_random = f(x_random)
monte_carlo_integral = (b - a) * np.mean(y_random)

print(analytical_integral, quad_result, monte_carlo_integral)
