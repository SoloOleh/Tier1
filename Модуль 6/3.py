def add_employee_to_file(record, path):
    fh = open(path, "a")
    fh.write(record + "\n")  # Додаємо символ переводу рядка
    fh.close()
path = '/Users/solo/Desktop/IT/Repository/Tier1/Модуль 6/test.txt'
record = "Drake Mikelsson,19"
add_employee_to_file(record, path)

record = ("Mikelsson,19") # можна без дужок
add_employee_to_file(record, path)

# альтернатива ментора
# def add_employee_to_file(record, path):
#     file = open(path, 'a')
#     file.write(f'{record}\n')
#     file.close()