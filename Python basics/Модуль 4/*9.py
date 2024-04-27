# from pathlib import Path

# p = Path('/home/user/Downloads')  # p Вказує на теку /home/user/Downloads
# # print(p)

# У Path є ряд корисних методів та атрибутів:
# p.parent вказує на батьківську теку;
# p.name повертає лише ім'я (рядок) теки або файлу, на який вказує p;
# p.is_dir() повертає True, якщо p вказує на теку, та False, якщо на файл або такий шлях не існує;
# p.is_file() повертає True, якщо p вказує на файл, та False, якщо на теку, або такий шлях не існує;
# p.iterdir() повертає ітератор по всіх файлах та теках усередині теки p;

# from pathlib import Path
# p = Path('/home/user/Downloads')  # p Вказує на теку /home/user/Downloads
# for i in p.iterdir():
#     print(i.name)  # Виведе у циклі імена всіх тек та файлів у /home/user/Downloads
from pathlib import Path
def parse_folder(path):
    files = []
    folders = []

    for element in path.iterdir():
        if element.is_dir():
            folders.append(element.name)
        else:
            files.append(element.name)
    return (files, folders)