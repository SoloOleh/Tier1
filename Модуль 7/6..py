def make_request(keys, values):
    if len(keys) != len(values):
        return {}

    return dict(zip(keys, values))


def make_request(keys, values):
    # Якщо довжини списків keys і values не збігаються, повертаємо порожній словник
    if len(keys) != len(values):
        return {}

    # Створюємо порожній словник
    request_dict = {}
    
    # Заповнюємо словник парами ключ-значення з відповідних елементів списків keys і values
    for i in range(len(keys)):
        request_dict[keys[i]] = values[i]
    
    # Повертаємо сформований словник
    return request_dict

# Приклад використання функції
keys = ["name", "age", "city"]
values = ["John", 30, "New York"]
request = make_request(keys, values)
print(request)  # Виведе: {'name': 'John', 'age': 30, 'city': 'New York'}