from datetime import datetime, timedelta

class Birthday:
    def __init__(self, birthday_str):
        self.day, self.month, self.year = self.parse_birthday(birthday_str)

    @staticmethod
    def parse_birthday(birthday_str):
        day, month, year = map(int, birthday_str.split('.'))
        return day, month, year

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

class Record:
    def __init__(self, name, phone=None, birthday=None):
        self.name = name
        self.phones = [] if phone is None else [phone]
        self.birthday = birthday

    def add_birthday(self, birthday_str):
        if self.validate_birthday(birthday_str):
            self.birthday = Birthday(birthday_str)

    def days_to_birthday(self):
        if self.birthday is None:
            return None
        today = datetime.now().date()
        next_birthday = datetime(today.year, self.birthday.month, self.birthday.day).date()
        if next_birthday < today:
            next_birthday = datetime(today.year + 1, self.birthday.month, self.birthday.day).date()
        return (next_birthday - today).days

    @staticmethod
    def validate_phone(phone):
        return len(phone) == 10 and phone.isdigit()

    @staticmethod
    def validate_birthday(birthday_str):
        try:
            day, month, year = map(int, birthday_str.split('.'))
            return 1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2100
        except ValueError:
            return False

class AddressBook:
    def __init__(self):
        self.records = []

    def add_record(self, name, phone=None):
        if self.validate_phone(phone):
            record = Record(name, phone)
            self.records.append(record)

    def get_record_by_name(self, name):
        for record in self.records:
            if record.name == name:
                return record
        return None

    def get_birthdays_per_week(self, n_days=7):
        today = datetime.now().date()
        birthdays = []
        for record in self.records:
            if record.birthday is not None:
                days_to_birthday = record.days_to_birthday()
                if days_to_birthday is not None and days_to_birthday < n_days:
                    birthdays.append((record.name, str(record.birthday), days_to_birthday))
        return sorted(birthdays, key=lambda x: x[2])

def add_contact(book, name, phone):
    book.add_record(name, phone)

def change_phone(book, name, new_phone):
    record = book.get_record_by_name(name)
    if record:
        if book.validate_phone(new_phone):
            record.phones = [new_phone]
        else:
            print("Неправильний формат номера телефону")
    else:
        print(f"Контакт з іменем '{name}' не знайдено")

def show_phone(book, name):
    record = book.get_record_by_name(name)
    if record:
        print(f"{name}: {', '.join(record.phones)}")
    else:
        print(f"Контакт з іменем '{name}' не знайдено")

def show_all_contacts(book):
    for record in book.records:
        phones = ', '.join(record.phones)
        birthday = str(record.birthday) if record.birthday else '-'
        print(f"{record.name}: {phones}, {birthday}")

def add_birthday(book, name, birthday_str):
    record = book.get_record_by_name(name)
    if record:
        if record.validate_birthday(birthday_str):
            record.add_birthday(birthday_str)
        else:
            print("Неправильний формат дати народження. Використовуйте формат ДД.ММ.РРРР")
    else:
        print(f"Контакт з іменем '{name}' не знайдено")

def show_birthday(book, name):
    record = book.get_record_by_name(name)
    if record and record.birthday:
        print(f"{name}: {record.birthday}")
    else:
        print(f"Контакт з іменем '{name}' не знайдено або не має дня народження")

def list_birthdays_per_week(book):
    birthdays = book.get_birthdays_per_week()
    if birthdays:
        print("Дні народження на наступний тиждень:")
        for name, birthday, days in birthdays:
            print(f"{name}: {birthday} (через {days} днів)")
    else:
        print("На наступному тижні немає днів народжень")

def greet():
    print("Привіт! Я бот для керування адресною книгою.")

def main():
    book = AddressBook()

    while True:
        command = input("Введіть команду: ").strip().lower()

        if command == "add":
            name, phone = input("Введіть ім'я та номер телефону через пробіл: ").split(" ", 1)
            add_contact(book, name, phone)
        elif command == "change":
            name, new_phone = input("Введіть ім'я та новий номер телефону через пробіл: ").split(" ", 1)
            change_phone(book, name, new_phone)
        elif command == "phone":
            name = input("Введіть ім'я: ")
            show_phone(book, name)
        elif command == "all":
            show_all_contacts(book)
        elif command == "add-birthday":
            name, birthday_str = input("Введіть ім'я та дату народження (ДД.ММ.РРРР) через пробіл: ").split(" ", 1)
            add_birthday(book, name, birthday_str)
        elif command == "show-birthday":
            name = input("Введіть ім'я: ")
            show_birthday(book, name)
        elif command == "birthdays":
            list_birthdays_per_week(book)
        elif command == "hello":
            greet()
        elif command in ["close", "exit"]:
            print("До побачення!")
            break
        else:
            print("Невідома команда. Спробуйте ще раз.")

if __name__ == "__main__":
    main()