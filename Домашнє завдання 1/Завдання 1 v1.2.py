from collections import defaultdict
from datetime import datetime, timedelta


def get_birthdays_per_week(users):
  """
  Функція виводить список користувачів, яких потрібно привітати з днем народження на тижні.

  Args:
    users: Список словників, де кожен словник містить ключі "name" та "birthday".

  Returns:
    None. Виводить у консоль список користувачів, яких потрібно привітати по днях на наступному тижні.
  """

  birthdays = defaultdict(list)
  today = datetime.today().date()

  for user in users:
    name = user["name"]
    birthday = user["birthday"].date()
    birthday_this_year = birthday.replace(year=today.year)

    if birthday_this_year < today:
      birthday_this_year = birthday_this_year.replace(year=today.year + 1)

    delta_days = (birthday_this_year - today).days

    if delta_days < 7:
      weekday = (today + timedelta(days=delta_days)).weekday()
      if weekday in (5, 6):
        weekday = 0

      birthdays[WEEKDAYS[weekday]].append(name)

  for weekday, names in birthdays.items():
    print(f"{weekday}: {', '.join(names)}")


WEEKDAYS = {
  0: "Monday",
  1: "Tuesday",
  2: "Wednesday",
  3: "Thursday",
  4: "Friday",
  5: "Saturday",
  6: "Sunday",
}


# Приклад використання
users = [
  {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
  {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
  {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)},
  {"name": "Jill Valentine", "birthday": datetime(1983, 3, 31)},
]

get_birthdays_per_week(users)


