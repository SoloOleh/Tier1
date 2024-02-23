def get_employees_by_profession(path, profession):
    with open(path, 'r') as file:
        lines = file.readlines()

    # Вибираємо імена співробітників з вказаною професією
    employees = [line.replace(profession, "").strip() for line in lines if profession in line]
    
    # Об'єднуємо імена в один рядок через пробіл
    return ' '.join(employees)