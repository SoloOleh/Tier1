from datetime import datetime, timedelta
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
        self.validate()

    def validate(self):
        if not (len(self.value) == 10 and self.value.isdigit()):
            raise ValueError("Phone number must be 10 digits long")

class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate()

    def validate(self):
        try:
            datetime.strptime(self.value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Birthday must be in DD.MM.YYYY format")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return True
        return False

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                return True
        return False

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):
        phones_str = "; ".join(p.value for p in self.phones)
        birthday_str = f", Birthday: {self.birthday}" if self.birthday else ""
        return f"Name: {self.name.value}, Phones: {phones_str}{birthday_str}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)
    
    def delete_record(self, name):
        if name in self.data:
            del self.data[name]

    def get_birthdays_per_week(self):
        today = datetime.now()
        upcoming_birthdays = []
        for record in self.data.values():
            if record.birthday:
                birthday_date = datetime.strptime(record.birthday.value, "%d.%m.%Y")
                birthday_this_year = birthday_date.replace(year=today.year)
                delta_days = (birthday_this_year - today).days
                if 0 <= delta_days <= 7:
                    upcoming_birthdays.append(record.name.value)
        return upcoming_birthdays

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Please provide enough information."
    return inner

@input_error
def add_contact(args, book):
    name, phone = args
    if name in book:
        return "Contact already exists. Try updating the phone number."
    record = Record(name)
    record.add_phone(phone)
    book.add_record(record)
    return "Contact added."

@input_error
def change_contact(args, book):
    name, new_phone = args
    record = book.find(name)
    if record:
        record.phones = [Phone(new_phone)]  # Replace all phones with a new one for simplicity
        return "Contact updated."
    else:
        raise KeyError

@input_error
def show_phone(args, book):
    name = args[0]
    record = book.find(name)
    if record:
        return ', '.join(phone.value for phone in record.phones)
    else:
        raise KeyError

@input_error
def show_all(book):
    if book.data:
        return '\n'.join([str(record) for record in book.data.values()])
    else:
        return "No contacts saved."

@input_error
def add_birthday(args, book):
    name, birthday = args
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return "Birthday added."
    else:
        raise KeyError

@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if record and record.birthday:
        return f"Birthday of {name}: {record.birthday.value}"
    else:
        return "Birthday not found."

@input_error
def list_birthdays(book):
    birthdays = book.get_birthdays_per_week()
    if birthdays:
        return f"Birthdays next week: {', '.join(birthdays)}"
    else:
        return "No birthdays next week."

def main():
    book = AddressBook()
    command_handlers = {
        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": show_all,
        "add-birthday": add_birthday,
        "show-birthday": show_birthday,
        "birthdays": list_birthdays,
        "hello": lambda _, __: "How can I help you?"
    }

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = user_input.split(maxsplit=1)
        args = args[0].split() if args else []

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        handler = command_handlers.get(command)
        if handler:
            print(handler(args, book))
        else:
            print("Invalid command.")

main()

