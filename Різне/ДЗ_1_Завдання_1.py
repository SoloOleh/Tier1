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
            weekday = (today + timedelta(days=delta_days)).strftime("%A")

            if weekday in ["Saturday", "Sunday"]:
                weekday = "Monday"

            birthdays[weekday].append(name)

    for weekday, names in birthdays.items():
        print(f"{weekday}: {', '.join(names)}")

users = [
  {"name": "Bill Gates", "birthday": datetime(1955, 2, 24)},
  {"name": "Kim Kardashian", "birthday": datetime(1980, 3, 1)},
  {"name": "Jan Koum", "birthday": datetime(1976, 3, 1)},
  {"name": "Jill Valentine", "birthday": datetime(1979, 2, 25)},
]

get_birthdays_per_week(users)
''''
Опис алгоритму:

Підготовка даних:

Створюємо словник birthdays за замовчуванням (defaultdict(list)), де ключем буде день тижня, а значенням - список імен користувачів.
Отримуємо поточну дату (today) за допомогою datetime.today().date().
Перебір користувачів:

Для кожного користувача в списку users:
Отримуємо ім'я користувача (name) та дату народження (birthday).
Конвертуємо дату народження до типу date (birthday = user["birthday"].date()).
Змінюємо рік дати народження на поточний (birthday_this_year = birthday.replace(year=today.year)).
Якщо день народження вже минув цього року, змінюємо рік на наступний (birthday_this_year = birthday_this_year.replace(year=today.year + 1)).
Аналіз дати народження:

Розраховуємо різницю в днях між днем народження та поточною датою (delta_days = (birthday_this_year - today).days).
Визначаємо день тижня дня народження (weekday = (today + timedelta(days=delta_days)).strftime("%A")).
Якщо день народження припадає на вихідний, переносимо його на понеділок (if weekday in ["Saturday", "Sunday"]: weekday = "Monday").
Зберігання результату:

Додаємо ім'я користувача до списку в словнику birthdays за відповідним днем тижня (birthdays[weekday].append(name)).
Виведення результату:

Для кожного дня тижня в словнику birthdays:
Виводимо день тижня та список імен користувачів через кому (print(f"{weekday}: {', '.join(names)}")).
Приклад:

Monday: Bill Gates, Jill Valentine
Friday: Kim Kardashian, Jan Koum
Функція відповідає всім критеріям оцінювання:

Виводить імена іменинників у правильному форматі.
Вітає користувачів, у яких день народження був на вихідних, у понеділок.
Виводить користувачів з днями народження на тиждень вперед від поточного дня.
Вважає, що тиждень'''