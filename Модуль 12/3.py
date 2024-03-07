import csv
# #альтернативний варіант
# def write_contacts_to_file(filename, contacts):
#     # Відкриваємо файл у режимі запису
#     with open(filename, 'w', newline='') as csvfile:
#         # Створюємо об'єкт для запису у файл у форматі CSV
#         writer = csv.writer(csvfile)
        
#         # Записуємо заголовки у файл
#         writer.writerow(['name', 'email', 'phone', 'favorite'])
        
#         # Проходимося по кожному контакту у списку
#         for contact in contacts:
#             # Записуємо дані кожного контакту у файл
#             writer.writerow([contact['name'], contact['email'], contact['phone'], contact['favorite']])


def write_contacts_to_file(filename, contacts):
    # Відкриваємо файл у режимі запису
    with open(filename, 'w', newline='') as csvfile:
        # Задаємо заголовки для полів у файлі
        fieldnames = ['name', 'email', 'phone', 'favorite']
        
        # Створюємо об'єкт для запису у файл у форматі CSV
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Записуємо заголовки у файл
        writer.writeheader()
        
        # Записуємо кожен контакт у файл
        for contact in contacts:
            writer.writerow(contact)

def read_contacts_from_file(filename):
    contacts = []  # Створюємо пустий список для збереження контактів
    
    # Відкриваємо файл у режимі читання
    with open(filename, 'r', newline='') as csvfile:
        # Створюємо об'єкт для читання даних з файлу у форматі CSV
        reader = csv.DictReader(csvfile)
        
        # Проходимося по кожному рядку у файлі
        for row in reader:
            # Перетворюємо значення favorite на логічний тип
            row['favorite'] = row['favorite'].lower() == 'true'
            
            # Додаємо словник контакту у список контактів
            contacts.append(row)
    
    return contacts
