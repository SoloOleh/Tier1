from datetime import datetime, timedelta


def get_birthdays_per_week(users):
  """
  Функція виводить список користувачів, яких потрібно привітати з днем народження на тижні.

  Args:
    users: список словників, де кожен словник містить ім'я та дату народження користувача.

  Returns:
    None.
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
      weekday = (today + timedelta(days=delta_days)).strftime("%A")

      if weekday in ["Saturday", "Sunday"]:
        weekday = "Monday"

      birthdays[weekday].append(name)

  for weekday, names in birthdays.items():
    print(f"{weekday}: {', '.join(names)}")


# Приклад використання
users = [
  {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
  {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
  {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)},
  {"name": "Jill Valentine", "birthday": datetime(1979, 3, 31)},
]

get_birthdays_per_week(users)
