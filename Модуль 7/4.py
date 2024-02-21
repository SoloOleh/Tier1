"""Функція видаляє з списків найбільше і найменше значення, 
  зливає їх в один список, сортує за зменшенням та повертає.

  Args:
      list_data: Список списків ([[1,2,3],[3,4], [5,6]]).

  Returns:
      Відсортований список без екстремальних значень."""

def data_preparation(list_data):
    # Створення пустого списку для результату
    result = []
    for sublist in list_data:
        # Якщо в підсписку більше двох елементів, видаляємо найбільший та найменший
        if len(sublist) > 2:
            sublist.remove(max(sublist))
            sublist.remove(min(sublist))
        # Додавання оновленого підсписку до результату
        result.extend(sublist)
    # Сортування результату за спаданням
    result.sort(reverse=True)
    return result

# Тестування функції
data = [[1,2,3], [3,4], [5,6]]
result = data_preparation(data)
print(result)

# print(data_preparation([[1, 2, 3], [3, 4], [5, 6]]))  # Приклад вхідних даних скорочено
