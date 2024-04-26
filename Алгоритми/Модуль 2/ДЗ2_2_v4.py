from collections import deque

def check_palindrome(string):
    # Видаляємо пробіли та переводимо рядок в нижній регістр
    formatted_string = string.lower().strip()
    
    # Створюємо двосторонню чергу (deque)
    char_deque = deque(formatted_string)
    
    # Додаємо символи рядка до черги
    for char in string:
        char_deque.append(char)
    
    # Порівнюємо символи з обох кінців черги, поки черга не опустіється
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False 
    return True 

# Приклад використання
input_string = "Козак з казок"
print(check_palindrome(input_string))



