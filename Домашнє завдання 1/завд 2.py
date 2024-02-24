def parse_input(user_input):
    """
    Розбиває введений рядок на команду та аргументи.

    Args:
        user_input (str): Введений користувачем рядок.

    Returns:
        tuple: Кортеж, що містить команду та список аргументів.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    """
    Додає новий контакт до телефонної книги.

    Args:
        args (list): Список аргументів, що містить ім'я та номер телефону.
        contacts (dict): Словник, що містить телефонну книгу.

    Returns:
        str: Повідомлення про успішне додавання контакту.
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    """
    Змінює номер телефону для існуючого контакту.

    Args:
        args (list): Список аргументів, що містить ім'я та новий номер телефону.
        contacts (dict): Словник, що містить телефонну книгу.

    Returns:
        str: Повідомлення про успішне оновлення контакту або повідомлення про помилку.
    """
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(args, contacts):
    """
    Виводить номер телефону для існуючого контакту.

    Args:
        args (list): Список аргументів, що містить ім'я контакту.
        contacts (dict): Словник, що містить телефонну книгу.

    Returns:
        str: Номер телефону або повідомлення про помилку.
    """
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def show_all(contacts):
    """
    Виводить список усіх збережених контактів з номерами телефонів.

    Args:
        contacts (dict): Словник, що містить телефонну книгу.

    Returns:
        str: Список контактів.
    """
    all_contacts = ""
    for name, phone in contacts.items():
        all_contacts += f"{name}: {phone}\n"
    return all_contacts

def main():
    """
    Запускає бота.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

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
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
