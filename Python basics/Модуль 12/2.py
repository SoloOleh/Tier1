import json

def write_contacts_to_file(filename, contacts):
    # Створюємо словник для зберігання контактів
    data = {"contacts": contacts}
    # Відкриваємо файл для запису у режимі тексту
    with open(filename, "w") as file:
        # Записуємо дані у файл у форматі JSON
        json.dump(data, file, indent=2)

def read_contacts_from_file(filename):
    # Відкриваємо файл для читання у режимі тексту
    with open(filename, "r") as file:
        # Зчитуємо дані з файлу
        data = json.load(file)
        # Повертаємо список контактів
        return data["contacts"]

# Приклад використання:
contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False
    },
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "(123) 456-7890",
        "favorite": True
    }
]

filename = "contacts.json"

# Записуємо контакти у файл
write_contacts_to_file(filename, contacts)

# Читаємо контакти з файлу
read_contacts = read_contacts_from_file(filename)

# Виводимо результат
print(read_contacts)
