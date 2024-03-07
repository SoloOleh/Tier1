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

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Please provide enough information."
    return inner

def parse_input(user_input):
    command, *args = user_input.split(maxsplit=2)
    command = command.strip().lower()
    return command, args

@input_error
def add_contact(args, book):
    name, phone = args
    if name in book:
        return "Contact already exists. Use change to update the phone number."
    record = Record(name)
    record.add_phone(phone)
    book.add_record(record)
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name].add_phone(new_phone)
        return "Contact updated."
    else:
        return "Contact not found."

# @input_error
# def change_contact(args, contacts):
#     name, new_phone = args
#     if name in contacts:
#         contacts[name] = new_phone
#         return "Contact updated."
#     else:
#         return "Contact not found."

@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError

@input_error
def show_all(contacts):
    if contacts:
        return '\n'.join([f"{name}: {phone}" for name, phone in contacts.items()])
    else: # в умові завдання цього не було, проте я добавив по аналогії з іншими функціями
        return "No contacts saved."

@input_error
def add_birthday(args, contacts):
    name, birthday = args
    if name not in contacts:
        raise KeyError("Contact not found.")
    contacts[name].add_birthday(birthday)
    return "Birthday added."

@input_error
def show_birthday(args, contacts):
    name = args[0]
    if name in contacts:
        if contacts[name].birthday:
            return f"{name}'s birthday is on {contacts[name].birthday.value}."
        else:
            return f"{name} has no specified birthday."
    else:
        raise KeyError("Contact not found.")
    
@input_error
def show_upcoming_birthdays(contacts):
    users = [{"name": record.name.value, "birthday": datetime.strptime(record.birthday.value, "%d.%m.%Y")} for record in contacts.values() if record.birthday]
    get_birthdays_per_week(users)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "add-birthday":
            print(add_birthday(args, contacts))
        elif command == "show-birthday":
            print(show_birthday(args, contacts))
        elif command == "birthdays":
            show_upcoming_birthdays(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if not self.validate():
            raise ValueError("Phone number must be 10 digits long")
    
    def validate(self):
        return len(self.value) == 10 and self.value.isdigit()

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        phone = self.find_phone(old_phone)
        phone.value = new_phone

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def add_birthday(self, birthday): 
        self.birthday = Birthday(birthday)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday.value if self.birthday else 'Not specified'}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
    
    def get_birthdays_per_week(self):
        users = [{"name": record.name.value, "birthday": datetime.strptime(record.birthday.value, "%d.%m.%Y")} for record in self.data.values() if record.birthday]
        get_birthdays_per_week(users)


class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        if not self.validate():
            raise ValueError("Birthday must be in the format DD.MM.YYYY")
    
    def validate(self):
        try:
            datetime.strptime(self.value, "%d.%m.%Y")
            return True
        except ValueError:
            return False