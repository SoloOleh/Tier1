import copy


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


def copy_class_person(person):
    # Використовуємо copy.copy для створення "поверхневої" копії об'єкта
    copy_person = copy.copy(person)
    return copy_person
    # або return copy.copy(person)



person = Person(
    "Allen Raymond",
    "nulla.ante@vestibul.co.uk",
    "(992) 914-3792",
    False,
)

copy_person = copy_class_person(person)

# Перевіряємо, чи копія не є посиланням на оригінал
print(copy_person == person)  # False

# Перевіряємо, чи значення атрибутів однакові
print(copy_person.name == person.name)  # True