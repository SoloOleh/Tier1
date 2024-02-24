import datetime
from collections import defaultdict

def get_birthdays_per_week(users):
    today = datetime.datetime.today().date()
    next_week = today + datetime.timedelta(days=7)
    birthdays = defaultdict(list)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        # Adjust for already passed birthdays this year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Calculate the number of days until the birthday
        delta_days = (birthday_this_year - today).days

        # If the birthday is within the next 7 days
        if 0 <= delta_days < 7:
            day_of_week = birthday_this_year.weekday()

            # If it's on the weekend, move to Monday
            if day_of_week in [5, 6]:  # Saturday and Sunday
                day_of_week = 0  # Monday

            day_name = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][day_of_week]
            birthdays[day_name].append(name)

    # Print the birthdays per day of the week
    for day, names in birthdays.items():
        print(f"{day}: {', '.join(names)}")

# Example usage
users = [
    {"name": "Bill Gates", "birthday": datetime.datetime(1955, 2, 25)},
    {"name": "Jan Koum", "birthday": datetime.datetime(1976, 2, 24)}
]

get_birthdays_per_week(users)
