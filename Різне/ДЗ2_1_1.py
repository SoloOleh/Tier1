def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "No such contact found."
        except IndexError:
            return "Please provide enough information."
    return inner

@input_error
def remove_contact(args, contacts):
    name = args[0]
    del contacts[name]
    return "Contact removed."

@input_error
def get_phone(args, contacts):
    name = args[0]
    return contacts[name]

@input_error
def update_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated."

def main_loop():
    contacts = {}
    while True:
        user_input = input("Enter command: ")
        if user_input.lower() == "exit":
            break
        command, *args = user_input.split()

        if command.lower() == "add":
            print(add_contact(args, contacts))
        elif command.lower() == "remove":
            print(remove_contact(args, contacts))
        elif command.lower() == "show":
            print(get_phone(args, contacts))
        elif command.lower() == "update":
            print(update_contact(args, contacts))
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main_loop()
