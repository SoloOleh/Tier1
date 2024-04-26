from collections import deque

def is_palindrome(string):
    # Видаляємо пробіли та переводимо рядок в нижній регістр
    string = string.replace(" ", "").lower()
    
    # Створюємо двосторонню чергу (deque)
    char_queue = deque()
    
    # Додаємо символи рядка до черги
    for char in string:
        char_queue.append(char)
    
    # Порівнюємо символи з обох кінців черги, поки черга не опустіється
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    
    return True

# Приклад використання
input_string = "A man a plan a canal Panama"
print(is_palindrome(input_string))  # Повинно вивести True
