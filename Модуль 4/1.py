# persons = ['Jane', 'Steve', 'Moris']
# print(persons[1])  # Steve

# persons = ['Jane', 'Steve', 'Moris']
# persons[1] = 'Niv'
# print(persons)  # ['Jane', 'Niv', 'Moris']

# data = [4, 3, 7.5]
# sum = 0
# for value in data:
#     sum = sum + value
# print(sum)  # 14.5


def amount_payment(payment):
    total_payment = 0  # Ініціалізуємо змінну для зберігання загальної суми платежів
    for amount in payment:  # Проходимося по кожному елементу списку платежів
        if amount > 0:  # Перевіряємо, чи платіж додатній
            total_payment += amount  # Додаємо платіж до загальної суми
    return total_payment  # Повертаємо загальну суму платежів

# Приклад використання:
payments = [100, -50, 200, -75, 50]
print(amount_payment(payments))  # Виведе: 350 (100 + 200 + 50)


