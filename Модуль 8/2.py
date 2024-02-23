from datetime import date

def get_days_in_month(month, year):
    # Перевірка на високосний рік
    if month == 2: # Лютий
        if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
            return 29
        else:
            return 28

    # Місяці з 31 днем
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31

    # Всі інші місяці мають 30 днів
    return 30

# Перевірка функції
print(get_days_in_month(2, 2020)) # Високосний рік
print(get_days_in_month(2, 2021)) # Звичайний рік
