from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    # Ініціалізуємо словник для зберігання ім'янників по днях тижня
    birthdays_per_week = defaultdict(list)
    
    # Отримуємо поточну дату
    today = datetime.today().date()
    
    # Перебираємо користувачів
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        
        # Визначаємо день народження цього року
        birthday_this_year = birthday.replace(year=today.year)
        
        # Перевіряємо, чи минув вже день народження цього року
        if birthday_this_year < today:
            # Якщо так, то розглядаємо дату наступного року
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # Визначаємо різницю між днем народження та поточним днем
        delta_days = (birthday_this_year - today).days
        
        # Визначаємо день тижня дня народження
        birthday_weekday = (today + timedelta(days=delta_days)).strftime('%A')
        
        # Якщо день народження вихідний, переносимо на понеділок
        if delta_days >= 5:
            birthday_weekday = "Monday"
        
        # Зберігаємо ім'я користувача в відповідний день тижня
        birthdays_per_week[birthday_weekday].append(name)
    
    # Виводимо результат
    for day, names in birthdays_per_week.items():
        print(f"{day}: {', '.join(names)}")

# Приклад використання
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)},
    {"name": "Jill Valentine", "birthday": datetime(1987, 5, 14)},
]

get_birthdays_per_week(users)

    
    
    