def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter user name."
        except IndexError:
            return "Index out of range."
        except Exception as e:
            return f"An error occurred: {str(e)}"
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def search_contact(args, contacts):
    name = args[0]
    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}"
    else:
        return f"Contact {name} not found."

@input_error
def remove_contact(args, contacts):
    name = args[0]
    if name in contacts:
        del contacts[name]
        return f"Contact {name} removed."
    else:
        return f"Contact {name} not found."
