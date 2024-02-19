def read_employees_from_file(path):
    file = open(path, 'r')
    employees = []
    for line in file:
        employees.append(line.strip())
    file.close()
    return employees