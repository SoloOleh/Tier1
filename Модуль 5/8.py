# import re

# message = "I am 25 years old"
# age = re.search('\d+', message)
# print(age)  # <re.Match object; span=(5, 7), match='25'>

# s = "I am 25 years old."
# age = re.search('\d+', message)
# print(age.group())  # 25

# # Функція search — "ледача" і знаходить тільки першу відповідність заданій умові.

# # Об'єкт Match має властивості та методи, що використовуються для отримання інформації про пошук та результат:

# # Match.span() повертає кортеж, що містить початкову та кінцеву позиції збігу.
# # Match.string повертає рядок, переданий у функцію,
# # Match.group() повертає частину рядка, в якому був збіг

# import re

# def find_word(text, word):
#     # Застосовуємо регулярний вираз для пошуку слова в тексті
#     match = re.search(re.escape(word), text)
    
#     # Якщо знайдено збіг, формуємо словник з деталями пошуку
#     if match:
#         return {
#             'result': True,
#             'first_index': match.start(),
#             'last_index': match.end(),
#             'search_string': match.group(),
#             'string': text
#         }
#     # Якщо збіг не знайдено, повертаємо словник з відповідними значеннями
#     else:
#         return {
#             'result': False,
#             'first_index': None,
#             'last_index': None,
#             'search_string': word,
#             'string': text
#         }

# # Приклади використання функції
# print(find_word(
#     "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
#     "Python"))

# print(find_word(
#     "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
#     "python"))

import re


def find_word(text, word):
  """
  Функція знаходить слово в тексті та повертає словник з результатом.

  Args:
      text: Рядок, в якому будемо шукати слово.
      word: Слово, яке шукаємо.

  Returns:
      Словник з результатом пошуку.
  """
  search_result = re.search(word, text)

  if search_result:
    return {
        "result": True,
        "first_index": search_result.start(),
        "last_index": search_result.end(),
        "search_string": search_result.group(),
        "string": text,
    }
  else:
    return {
        "result": False,
        "first_index": None,
        "last_index": None,
        "search_string": word,
        "string": text,
    }
print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "Python"))

print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "python"))

