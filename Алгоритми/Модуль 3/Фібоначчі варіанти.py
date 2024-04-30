def fibonacci(n):
    if n <= 1: # базовий випадок
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2) # рекурсивний випадок

print(fibonacci(10)) # виведе 55

def fibonacci_iterative(n): #ітерація
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

# Тестуємо функцію
print(fibonacci_iterative(10))  # Виведе: 55

def fibonacci_memo(n, memo={}): #мемоізація
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    else:
        value = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
        memo[n] = value
        return value


from functools import lru_cache

@lru_cache(maxsize=None)  # Unbounded cache
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
#Тепер кожне попередньо обчислене число Фібоначчі зберігається у кеші, що робить повторні виклики функції fibonacci для тих самих значень n неймовірно швидкими. 
