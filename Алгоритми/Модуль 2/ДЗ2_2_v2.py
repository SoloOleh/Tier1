from collections import deque

def check_palindrome(string):
  """
  Ця функція перевіряє, чи є рядок паліндромом, використовуючи двосторонню чергу (deque).

  Args:
    рядок: Рядок, який потрібно перевірити.

  Returns:
    True, якщо рядок є паліндромом, False - якщо ні.
  """

  # Очищення рядка від пробілів та переведення до нижнього регістру.
  string = string.lower().strip()

  # Створення двосторонньої черги.
  dq = deque(string)

  # Порівняння символів з обох кінців черги.
  while len(dq) > 1:
    first_symbol = dq.popleft()
    last_symbol = dq.pop()

    if first_symbol != last_symbol:
      return False

  return True

# Приклади використання
word = "А роза впала на лапу Азора"
sentence = "Я несу в корзині мак?"

if check_palindrome(word):
  print(f"{word} - це паліндром.")
else:
  print(f"{word} - не паліндром.")

if check_palindrome(sentence):
  print(f"{sentence} - це паліндром.")
else:
  print(f"{sentence} - не паліндром.")
