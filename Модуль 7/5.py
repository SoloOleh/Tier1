"""
  Функція генерує всі можливі підсписки заданого списку.

  Args:
      data: Список (наприклад, [1, 2, 3]).

  Returns:
      Список, що містить всі підсписки."""
def all_sub_lists(data):
  if len(data) == 0:
    return [[]]
  else:
    result = []
    for i in range(len(data)):
      # Додаємо всі підсписки, які починаються з i-го елемента
      for sublist in all_sub_lists(data[i+1:]):
        result.append([data[i]] + sublist)
      # Додаємо порожній список
      result.append([])
    return result

# Приклад використання
data = [4, 6, 1, 3]
all_sub_lists = all_sub_lists(data)
print(all_sub_lists)

