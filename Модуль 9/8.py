def positive_values(list_payment):
    # Функція для перевірки, чи є значення додатнім
    def is_positive(number):
        return number > 0

    # Фільтрування списку з використанням функції is_positive
    filtered_list = filter(is_positive, list_payment)

    # Повернення результату у вигляді списку
    return list(filtered_list)

# Тестування функції
payment = [100, -3, 400, 35, -100]
print(positive_values(payment))

