# import re
# p = re.sub(r'(blue|white|red)', 'color', 'blue socks and red shoes')
# print(p)  # color socks and color shoes


import re

def replace_spam_words(text, spam_words):
    # Функція для заміни заборонених слів на шаблон зірочок
    def replace_with_stars(match):
        return '*' * len(match.group())

    # Створюємо регулярний вираз для пошуку заборонених слів з урахуванням нечутливості до регістру
    # \b використовуємо для визначення меж слів, щоб замінювати лише цілі слова
    pattern = r'\b(' + '|'.join(re.escape(word) for word in spam_words) + r')\b'
    
    # Виконуємо заміну, використовуючи функцію replace_with_stars для генерації шаблону заміни
    result = re.sub(pattern, replace_with_stars, text, flags=re.IGNORECASE)
    
    return result

import re


def replace_spam_words(text, spam_words):
  """
  Функція замінює слова з списку spam_words у тексті text на шаблон з зірочок.

  Args:
    text: Рядок, який потрібно перевірити.
    spam_words: Список заборонених слів.

  Returns:
    Рядок з заміненими словами.
  """

  def replace_fn(matchobj):
    return "*" * len(matchobj.group(0))

  # Перетворюємо список spam_words у нечутливий до регістру
  spam_words_insensitive = [word.lower() for word in spam_words]

  # Складаємо регулярний вираз для пошуку слів зі списку spam_words_insensitive
  pattern = r"\b{}\b".format("|".join(spam_words_insensitive))

  # Замінюємо слова з шаблоном з зірочок
  return re.sub(pattern, replace_fn, text, flags=re.IGNORECASE)

# Приклад використання
text = "Це тестовий текст з деякими поганими словами."
spam_words = ["поганими", "словами"]

replaced_text = replace_spam_words(text, spam_words)

print(f"Оригінальний текст: {text}")
print(f"Замінений текст: {replaced_text}")
