# def write_employees_to_file(employee_list, path):
#     fh = open(path, "w")
#     text = fh.write(employee_list)
#     fh.close()
# path = '/Users/solo/Desktop/IT/Repository/Tier1/Модуль 6/test.txt'
# employee_list = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
# write_employees_to_file (employee_list, path)

# def write_employees_to_file(employee_list, path):
#     fh = open(path, "w")
#     for employee in employee_list:
#         fh.write(",".join(employee) + "\n")
#     fh.close()

# # Шлях до файлу та список співробітників
# path = '/Users/solo/Desktop/IT/Repository/Tier1/Модуль 6/test.txt'
# employee_list = [['Robert Stivenson,28'], ['Alex Denver,30'], ['Drake Mikelsson,19']]

# Виклик функції
# write_employees_to_file(employee_list, path)

def write_employees_to_file(employee_list, path): # [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
    file = open(path, 'w')
    employees = []
    for sub_list in employee_list:
        employees += sub_list
    for employee in employees:
        file.write(f'{employee}\n')
    file.close()
