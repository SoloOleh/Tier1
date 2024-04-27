# import re
# s = "I bought 7 nuts for 6$ and 10 bolts for 3$."
# numbers = re.findall('\d+', s)
# print(numbers)  # ['7', '6', '10', '3']

# import re
# s = "I bought 77 nuts for 6$ and 110 bolts for 3$."
# # print(re.findall("[0,1,3,6,7]", s))
# # print(re.findall("[^0,1,3,6,7]", s))

# import re
# s = "I bought 77 nuts for 6$ and 110 bolts for 3$."
# print(re.findall("(\d){3}", s))  # ['0']
# print(re.findall("[\d]{3}", s))  # ['110']

# import re
# s = "I bought 77 nuts for 6$ and 110 bolts for 3$."
# print(re.findall("(for|and)", s))  # ['for', 'and', 'for']



import re

def find_all_words(text, word):
    # Створюємо регулярний вираз для пошуку слова з урахуванням ігнорування регістру
    pattern = re.compile(re.escape(word), re.IGNORECASE)
    # Використовуємо findall для пошуку всіх входжень слова в тексті
    matches = pattern.findall(text)
    # Повертаємо список знайдених входжень
    return matches
