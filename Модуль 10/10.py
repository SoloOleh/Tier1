class IDException(Exception):
    pass

def add_id(id_list, employee_id):
    if not employee_id.startswith('01'):
        raise IDException("Employee ID must start with '01'")
    id_list.append(employee_id)
    return id_list

# gemimi
class IDException(Exception):
    pass


def add_id(id_list, employee_id):
  """
  Додає ідентифікатор користувача до списку, якщо він починається з '01'.

  Args:
    id_list: Список ідентифікаторів користувачів.
    employee_id: Ідентифікатор користувача, який потрібно додати.

  Raises:
    IDException: Якщо employee_id не починається з '01'.

  Returns:
    Оновлений список id_list з доданим employee_id.
  """

  if not employee_id.startswith('01'):
    raise IDException('Ідентифікатор користувача повинен починатися з "01"')
  id_list.append(employee_id)
  return id_list

# Приклад використання
try:
  id_list = ['0123456789']
  employee_id = '0198765432'
  new_id_list = add_id(id_list, employee_id)
  print(f'Список ідентифікаторів після додавання: {new_id_list}')
except IDException as e:
  print(f'Помилка: {e}')
