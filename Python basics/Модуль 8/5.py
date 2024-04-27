from decimal import Decimal, getcontext

def decimal_average(number_list, signs_count):
    # Встановлюємо точність виводу
    getcontext().prec = signs_count

    # Конвертуємо всі числа у списку до Decimal
    decimal_list = [Decimal(str(number)) for number in number_list]

    # Обчислюємо суму
    total = sum(decimal_list)

    # Обчислюємо середнє арифметичне
    average = total / len(decimal_list)

    return average

# Тестування функції
print(decimal_average([3, 5, 77, 23, 0.57], 6)) # Повинно повернути 21.714
print(decimal_average([31, 55, 177, 2300, 1.57], 9)) # Повинно повернути 512.91400
