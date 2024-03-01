def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, KeyError, IndexError):
            return "Помилка введення! Спробуйте ще раз."

    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Контакт додано."

@input_error
def find_contact(args, contacts):
    name = args[0]
    return f"Номер телефону {contacts[name]}."

@input_error
def show_contacts(contacts):
    for name, phone in contacts.items():
        print(f"{name}: {phone}")
    return "Список контактів показано."

@input_error
def del_contact(args, contacts):
    name = args[0]
    del contacts[name]
    return "Контакт видалено."

def main():
    contacts = {}
    while True:
        command = input("Введіть команду: ")
        args = command.split()

        if command == "exit":
            break

        if command == "help":
            print("Доступні команди:")
            print("    add name phone - додати контакт")
            print("    find name - знайти номер телефону")
            print("    show - показати список контактів")
            print("    del name - видалити контакт")
            continue

        try:
            handler[command](args, contacts)
        except KeyError:
            print("Невідома команда!")

if __name__ == "__main__":
    main()

