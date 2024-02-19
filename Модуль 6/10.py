# import shutil
# archive_name = shutil.make_archive('backup', 'zip')

# import shutil
# archive_name = shutil.make_archive('backup', 'zip', 'some_folder/inner')

# import shutil
# archive_name = shutil.make_archive('backup', 'zip', 'some_folder/inner')
# shutil.unpack_archive(archive_name, 'new_folder_for_data')

# import shutil
# for shortcut, description in shutil.get_archive_formats():
#     print('{:<10} | {:<10}'.format(shortcut, description))

import shutil

def create_backup(path, file_name, employee_residence):
    # Повний шлях до файлу
    full_file_path = path + '/' + file_name

    # Запис словника у бінарний файл
    with open(full_file_path, 'wb') as file:
        for name, country in employee_residence.items():
            # Формування рядка та його кодування
            line = f"{name} {country}\n".encode()
            file.write(line)

    # Ім'я для архіву, що не включає шлях
    archive_name = 'backup_folder'

    # Створення архіву, зазначаючи тільки назву теки, а не повний шлях
    shutil.make_archive(archive_name, 'zip', path)

    # Повернення шляху до архіву
    return path + '/' + f"{archive_name}.zip"

