import os
import shutil

def sort_files(src_dir, dst_dir="dist"):
  """
  Функція рекурсивно копіює файли з вихідної директорії до нової директорії, 
  сортуючи їх у піддиректорії за розширенням.

  Args:
      src_dir (str): Шлях до вихідної директорії.
      dst_dir (str, optional): Шлях до директорії призначення (за замовчуванням "dist").
  """

  try:
    # Створення директорії призначення, якщо вона не існує.
    if not os.path.exists(dst_dir):
      os.makedirs(dst_dir)

    # Перебір елементів у вихідній директорії.
    for entry in os.listdir(src_dir):
      full_path = os.path.join(src_dir, entry)

      # Перевірка, чи є елемент директорією.
      if os.path.isdir(full_path):
        sort_files(full_path, dst_dir)
      else:
        # Отримання розширення файлу.
        ext = os.path.splitext(entry)[1]

        # Створення шляху до піддиректорії за розширенням.
        ext_dir = os.path.join(dst_dir, ext[1:])

        # Створення піддиректорії, якщо вона не існує.
        if not os.path.exists(ext_dir):
          os.makedirs(ext_dir)

        # Копіювання файлу до відповідної піддиректорії.
        shutil.copy(full_path, ext_dir)

  except OSError as e:
    print(f"Помилка: {e}")

if __name__ == "__main__":
  # Парсинг аргументів командного рядка.
  if len(sys.argv) < 2:
    print("Використання: sort_files.py <вихідна_директорія> [директорія_призначення]")
    sys.exit(1)

  src_dir = sys.argv[1]
  dst_dir = sys.argv[2] if len(sys.argv) >= 3 else "dist"

  # Запуск сортування файлів.
  sort_files(src_dir, dst_dir)