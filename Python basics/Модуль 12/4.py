import pickle

class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        self.filename = filename
        if contacts is None:
            self.contacts = []
        else:
            self.contacts = contacts

    def save_to_file(self):
        # Відкриваємо файл у режимі запису бінарних даних
        with open(self.filename, 'wb') as file:
            # Використовуємо метод dump пакету pickle для серіалізації об'єкта в файл
            pickle.dump(self, file)

    def read_from_file(self):
        # Відкриваємо файл у режимі читання бінарних даних
        with open(self.filename, 'rb') as file:
            # Використовуємо метод load пакету pickle для десеріалізації об'єкта з файлу
            return pickle.load(file)

# Створюємо список контактів
contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]

# Створюємо екземпляр класу Contacts
persons = Contacts("user_class.dat", contacts)

# Зберігаємо об'єкт у файл
persons.save_to_file()

# Читаємо об'єкт з файлу
person_from_file = persons.read_from_file()  # Більше не потрібно передавати 'filename'

# Перевірка на рівність об'єктів та їхніх властивостей
print(persons == person_from_file)  # False
print(persons.contacts[0] == person_from_file.contacts[0])  # False
print(persons.contacts[0].name == person_from_file.contacts[0].name)  # True
print(persons.contacts[0].email == person_from_file.contacts[0].email)  # True
print(persons.contacts[0].phone == person_from_file.contacts[0].phone)  # True


