# for i in range(16):
#     s = "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(i)
#     print(s)

# width = 5
# for num in range(12):
#     print('{:^10} {:^10} {:^10}'.format(num, num ** 2, num ** 3))

# s = "{name} {last_name}".format(last_name="Dilan", name="Bob")
# print(s)  # Bob Dilan

# s = "{name!r} {last_name!s}".format(last_name="Dilan", name="Bob")
# print(s)  # 'Bob' Dilan

grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
  """
  Функція приймає словник оцінювання студентів за предмет 
  і повертає список відформатованих рядків.

  Args:
    students: словник, де ключем є ім'я студента, а значенням - його оцінка ECTS.

  Returns:
    Список відформатованих рядків.
  """
  grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
  formatted_list = []
  counter = 1
  for student, grade in students.items():
    formatted_row = "{:>4}|{:<10}|{:^5}|{:^5}".format(
        counter, student, grade, grades[grade]
    )
    formatted_list.append(formatted_row)
    counter += 1
  return formatted_list