from collections import deque

def is_palindrome(s: str) -> bool:
    # Підготовка рядка: переведення в нижній регістр і видалення пробілів
    formatted_string = ''.join(ch.lower() for ch in s if ch.isalnum())
    
    # Створення двосторонньої черги з символів підготовленого рядка
    char_deque = deque(formatted_string)
    
    # Перевірка на паліндром
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

# Тестуємо функцію з декількома прикладами
test_strings = ["Козак з казок"]
results = {s: is_palindrome(s) for s in test_strings}
print (results)
