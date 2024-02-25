from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    today = datetime.today().date()
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    birthdays = defaultdict(list)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if 0 <= delta_days < 7:
            day_of_week = weekdays[birthday_this_year.weekday()]
            if day_of_week in ["Saturday", "Sunday"]:
                day_of_week = "Monday"
            birthdays[day_of_week].append(name)

    for day in weekdays:
        if day in birthdays:
            print(f"{day}: {', '.join(birthdays[day])}")

# Прикладні дані для тестування
test_users = [
    {"name": "Alice wonder", "birthday": datetime(1990, 2, 24)},  # Субота цього року
    {"name": "Bob", "birthday": datetime(1985, 2, 20)},    # Середа минулого тижня
    {"name": "Carol", "birthday": datetime(1979, 2, 22)},  # П'ятниця цього тижня
    {"name": "Dave", "birthday": datetime(1992, 2, 25)},   # Понеділок наступного тижня
]

get_birthdays_per_week(test_users)


