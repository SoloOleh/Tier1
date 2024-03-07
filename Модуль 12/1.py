import pickle

def write_contacts_to_file(filename, contacts):
    with open(filename, 'wb') as file:
        pickle.dump(contacts, file)

def read_contacts_from_file(filename):
    with open(filename, 'rb') as file:
        contacts = pickle.load(file)
    return contacts

# Приклад використання:
contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "(123) 456-7890",
        "favorite": True,
    }
]

# Зберігаємо контакти у файл
write_contacts_to_file("contacts.pkl", contacts)

# Читаємо контакти з файлу
read_contacts = read_contacts_from_file("contacts.pkl")
print(read_contacts)
