from pathlib import Path
p = Path('/home/user/Downloads')    # p Вказує на папку /home/user/Downloads
print(p)

from pathlib import Path
p = Path()  # p Вказує на папку, з якої був запущений Python
print(p)

# p.parent вказує на батьківську папку;
# p.name повертає лише ім'я (рядок) папки або файлу, на який вказує p;
# p.suffix повертає рядком розширення файлу, на який вказує p, починаючи з крапки;
p = Path('setup.py')
p.suffix    # '.py'
print(p.suffix)

# p.exists() повертає True або False, залежно від того, чи існує такий файл або папка;
# p.is_dir() повертає True, якщо p вказує на папку, та False, якщо на файл, або такий шлях не існує;
# p.is_file() повертає True, якщо p вказує на файл, та False, якщо на папку, або такий шлях не існує;
# p.iterdir() повертає ітератор за всіма файлам та папками всередині папки p;
from pathlib import Path
p = Path('/home/user/Downloads')    # p Вказує на папку /home/user/Downloads
for i in p.iterdir():
    print(i.name)   # Виведе у циклі імена всіх папок та файлів у /home/user/Downloads
