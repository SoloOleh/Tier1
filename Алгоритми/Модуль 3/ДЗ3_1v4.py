import os
import shutil
import argparse

def copy_files(source, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)
    for root, dirs, files in os.walk(source):
        for file in files:
            file_path = os.path.join(root, file)
            extension = os.path.splitext(file)[1][1:] or "no_extension"
            ext_dir = os.path.join(destination, extension)
            if not os.path.exists(ext_dir):
                os.makedirs(ext_dir)
            dest_file_path = os.path.join(ext_dir, file)
            try:
                shutil.copy2(file_path, dest_file_path)
            except Exception as e:
                print(f"Не вдалося скопіювати файл {file_path}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Копіює файли за розширеннями.")
    parser.add_argument("source_directory", type=str, help="Шлях до вихідної директорії.")
    parser.add_argument("destination_directory", type=str, nargs='?', default="./dist", help="Шлях до директорії призначення (за замовчуванням: ./dist).")
    args = parser.parse_args()
    
    copy_files(args.source_directory, args.destination_directory)
