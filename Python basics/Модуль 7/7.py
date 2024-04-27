def file_operations(path, additional_info, start_pos, count_chars):
    # Відкриття файлу в режимі додавання інформації
    with open(path, 'a') as file:
        # Запис додаткової інформації в кінець файлу
        file.write(additional_info)

    # Відкриття файлу для читання
    with open(path, 'r') as file:
        # Переміщення курсору на позицію start_pos
        file.seek(start_pos)
        # Читання та повернення рядка завдовжки count_chars
        return file.read(count_chars)

# Ця функція може бути використана для виконання описаних операцій на файлі.
# Однак для її роботи потрібно мати доступ до файлової системи.
