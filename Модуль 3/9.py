def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def number_of_groups(n, k):
    numerator = factorial(n)
    denominator = factorial(n - k) * factorial(k)
    return numerator // denominator

# Приклад використання:
n = 50  # загальна кількість учасників
k = 7   # кількість призів
result = number_of_groups(n, k)
print("Кількість різних списків переможців:", result)
