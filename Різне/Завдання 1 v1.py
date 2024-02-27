from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    today = datetime.today().date()
    birthdays = defaultdict(list)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            # Визначаємо день тижня, якщо вихідний - переносимо на понеділок
            day_of_week = birthday_this_year.weekday()
            if day_of_week == 5 or day_of_week == 6:  # Субота або неділя
                day_of_week = 0  # Понеділок

            weekday_name = birthday_this_year.strftime("%A")
            birthdays[weekday_name].append(name)

    for day, names in birthdays.items():
        print(f"{day}: {', '.join(names)}")

# Приклад використання:
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 2, 25)},
    {"name": "Jill Valentine", "birthday": datetime(1974, 11, 1)},
    # Додайте інших користувачів для тестування
]

get_birthdays_per_week(users)

