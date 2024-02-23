import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])

def convert_list(cats):
    if isinstance(cats[0], dict):  # перевіряємо, чи перший елемент - словник
        return [Cat(cat["nickname"], cat["age"], cat["owner"]) for cat in cats]
    elif isinstance(cats[0], Cat):  # перевіряємо, чи перший елемент - іменований кортеж Cat
        return [{"nickname": cat.nickname, "age": cat.age, "owner": cat.owner} for cat in cats]

# Приклад використання:
cats_namedtuple = [Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
cats_dict = [
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"}
]

# Переведення іменованих кортежів в словники:
print(convert_list(cats_namedtuple))

# Переведення словників в іменовані кортежі:
print(convert_list(cats_dict))


# або варіант gemini
import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats):
  """
  Функція convert_list конвертує список іменованих кортежів Cat в список словників 
  або навпаки.

  Args:
      cats: Список іменованих кортежів Cat або список словників.

  Returns:
      Список словників або список іменованих кортежів Cat.
  """

  if isinstance(cats[0], Cat):
    # Перетворюємо список іменованих кортежів Cat в список словників
    return [
        {"nickname": cat.nickname, "age": cat.age, "owner": cat.owner} for cat in cats
    ]
  else:
    # Перетворюємо список словників в список іменованих кортежів Cat
    return [Cat(**cat) for cat in cats] 