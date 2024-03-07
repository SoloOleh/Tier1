# first = 'Hello'
# second = 'world'
# sentence = f"{first} {second}!"  # Hello world!
# print (sentence)


# Створення словника
person = {"ім'я": "Олексій", "вік": 30, "місто": "Київ"}

# Додавання нового ключа/значення
person["робота"] = "Програміст"

# Видалення пари ключ/значення
del person["вік"]

# Доступ до елемента
print(person["ім'я"])  # Олексій
print(person)
