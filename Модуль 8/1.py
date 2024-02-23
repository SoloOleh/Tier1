from datetime import datetime

def get_days_from_today(date):
    # Розбиваємо рядок date на рік, місяць та день
    year, month, day = map(int, date.split('-'))

    # Створюємо об'єкт datetime з заданими роком, місяцем та днем
    given_date = datetime(year, month, day)

    # Отримуємо поточну дату
    current_date = datetime.now()

    # Обчислюємо різницю в днях між заданою датою та поточною датою
    delta = current_date - given_date

    # Повертаємо кількість днів як ціле число
    return delta.days

# Приклад використання функції
print(get_days_from_today("2020-10-09"))
