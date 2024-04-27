import random


def get_random_winners(quantity, participants):
  """
  Функція для випадкового вибору переможців розіграшу.

  Args:
      quantity: Кількість переможців.
      participants: Словник з зареєстрованими користувачами.

  Returns:
      Список унікальних ідентифікаторів переможців.
  """

  # Перевірка валідності кількості переможців
  if quantity > len(participants):
    return []

  # Отримання списку ключів словника
  participants_ids = list(participants.keys())

  # Перемішування списку
  random.shuffle(participants_ids)

  # Вибір випадкових переможців
  winners_ids = random.sample(participants_ids, k=quantity)

  return winners_ids

# Приклад використання
quantity = 2
participants = {
    "603d2cec9993c627f0982404": "test@test.com",
    "603f79022922882d30dd7bb6": "test11@test.com",
    "60577ce4b536f8259cc225d2": "test2@test.com",
    "605884760742316c07eae603": "vitanlhouse@gmail.com",
    "605b89080c318d66862db390": "elhe2013@gmail.com",
}

winners_ids = get_random_winners(quantity, participants)

print(f"Переможці: {winners_ids}")


