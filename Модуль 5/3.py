# def is_check_name(fullname, first_name):
#     return fullname.startswith(first_name)

def is_check_name(fullname, first_name):
  """
  Функція перевіряє, чи є рядок first_name префіксом рядка fullname.

  Args:
    fullname: Рядок з повним ім'ям.
    first_name: Рядок з ім'ям.

  Returns:
    True, якщо first_name є префіксом fullname, False - інакше.
  """
  if not fullname or not first_name:
    return False
  return fullname.startswith(first_name)

# Приклади використання
full_name = "Іван Петренко"

print(is_check_name(full_name, "Іван"))  # True
print(is_check_name(full_name, "ван"))  # False
print(is_check_name(full_name, "Петренко"))  # False
print(is_check_name(full_name, "Іван Петрович"))  # False
