def get_emails(list_contacts):
    # Визначаємо функцію, яка буде застосовуватися до кожного контакту в списку
    def extract_email(contact):
        return contact['email']

    # Використовуємо функцію map з функцією extract_email і списком контактів
    return list(map(extract_email, list_contacts))
