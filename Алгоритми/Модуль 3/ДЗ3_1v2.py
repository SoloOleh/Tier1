import os
import shutil

def copy_files(source, destination):
    """
    Копіює файли з вихідної директорії у цільову, сортуючи їх за розширеннями.
    """
    # Створюємо цільову директорію, якщо вона не існує
    if not os.path.exists(destination):
        os.makedirs(destination)
    
    # Перебираємо всі файли та директорії в директорії source
    for root, dirs, files in os.walk(source):
        for file in files:
            file_path = os.path.join(root, file)
            extension = os.path.splitext(file)[1][1:]  # Видаляємо крапку з розширення
            if extension == "":
                extension = "no_extension"
            ext_dir = os.path.join(destination, extension)
            if not os.path.exists(ext_dir):
                os.makedirs(ext_dir)
            dest_file_path = os.path.join(ext_dir, file)
            try:
                shutil.copy2(file_path, dest_file_path)
            except Exception as e:
                print(f"Не вдалося скопіювати файл {file_path}: {e}")

if __name__ == "__main__":
    # Задаємо шляхи в коді
    source_directory = '/path/to/source'  # Змініть на ваш фактичний шлях до вихідної директорії
    destination_directory = '/path/to/destination'  # Змініть на ваш фактичний шлях до директорії призначення

    copy_files(source_directory, destination_directory)
