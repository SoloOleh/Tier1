def caching_fibonacci():
    cache = {0: 0, 1: 1}  # Початкове кешування для перших двох чисел Фібоначчі

    def fibonacci(n):
        if n in cache:  # Якщо число вже є в кеші, просто повертаємо його
            return cache[n]
        else:
            # Якщо число немає в кеші, обчислюємо його рекурсивно і зберігаємо в кеші
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

    return fibonacci

# Тестування функції
fib = caching_fibonacci()
print(fib(10))  # Приклад використання функції
