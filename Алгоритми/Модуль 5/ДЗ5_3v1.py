import timeit

def boyer_moore(text, pattern):
    def build_shift_table(pattern):
        table = {}
        length = len(pattern)
        for index, char in enumerate(pattern[:-1]):
            table[char] = length - index - 1
        table.setdefault(pattern[-1], length)
        return table
    
    shift_table = build_shift_table(pattern)
    i = 0
    
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            return i
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))
    return -1

def kmp(main_string, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    
    lps = compute_lps(pattern)
    i = j = 0
    while i < len(main_string):
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j
        elif i < len(main_string) and pattern[j] != main_string[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

def rabin_karp(main_string, substring):
    def polynomial_hash(s, base=256, modulus=101):
        n = len(s)
        hash_value = 0
        for i, char in enumerate(s):
            power_of_base = pow(base, n - i - 1, modulus)
            hash_value = (hash_value + ord(char) * power_of_base) % modulus
        return hash_value
    
    substring_length = len(substring)
    main_string_length = len(main_string)
    base = 256
    modulus = 101
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)
    h_multiplier = pow(base, substring_length - 1, modulus)
    
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i+substring_length] == substring:
                return i
        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus
    return -1


# Зчитування вмісту статей
with open("/Users/solo/Desktop/IT/Repository/Tier1/стаття 1.txt", "r", encoding="iso-8859-1") as f:
    text1 = f.read()

with open("/Users/solo/Desktop/IT/Repository/Tier1/стаття 2.txt", "r", encoding="iso-8859-1") as f:
    text2 = f.read()

# Два різних підрядки для пошуку
real = "алгоритм"
fake = "qwerty"
pattern1 = real
pattern2 = fake

# Виміри часу для статті 1
print("Стаття 1:")
print(f"Бойєр-Мур ('{pattern1}'):    ", timeit.timeit(lambda: boyer_moore(pattern1, text1), number=1000))
print(f"Кнут-Морріс-Пратт ('{pattern1}'):", timeit.timeit(lambda: kmp(pattern1, text1), number=1000))
print(f"Рабін-Карп ('{pattern1}'):       ", timeit.timeit(lambda: rabin_karp(pattern1, text1), number=1000))
print(f"Бойєр-Мур ('{pattern2}'):    ", timeit.timeit(lambda: boyer_moore(pattern2, text1), number=1000))
print(f"Кнут-Морріс-Пратт ('{pattern2}'):", timeit.timeit(lambda: kmp(pattern2, text1), number=1000))
print(f"Рабін-Карп ('{pattern2}'):       ", timeit.timeit(lambda: rabin_karp(pattern2, text1), number=1000))

# Виміри часу для статті 2
print("\nСтаття 2:")
print(f"Бойєр-Мур ('{pattern1}'):    ", timeit.timeit(lambda: boyer_moore(pattern1, text2), number=1000))
print(f"Кнут-Морріс-Пратт ('{pattern1}'):", timeit.timeit(lambda: kmp(pattern1, text2), number=1000))
print(f"Рабін-Карп ('{pattern1}'):       ", timeit.timeit(lambda: rabin_karp(pattern1, text2), number=1000))
print(f"Бойєр-Мур ('{pattern2}'):    ", timeit.timeit(lambda: boyer_moore(pattern2, text2), number=1000))
print(f"Кнут-Морріс-Пратт ('{pattern2}'):", timeit.timeit(lambda: kmp(pattern2, text2), number=1000))
print(f"Рабін-Карп ('{pattern2}'):       ", timeit.timeit(lambda: rabin_karp(pattern2, text2), number=1000))

# Результати:
# Стаття 1:
# Бойєр-Мур ('алгоритм'):     0.7348292079987004
# Кнут-Морріс-Пратт ('алгоритм'): 0.8866600829642266
# Рабін-Карп ('алгоритм'):        5.200790249975398
# Бойєр-Мур ('qwerty'):     0.7383884999435395
# Кнут-Морріс-Пратт ('qwerty'): 0.8892237920081243
# Рабін-Карп ('qwerty'):        5.2070999999996275

# # Стаття 2:
# Бойєр-Мур ('алгоритм'):     1.0440726249944419
# Кнут-Морріс-Пратт ('алгоритм'): 1.284499500063248
# Рабін-Карп ('алгоритм'):        7.852505458053201
# Бойєр-Мур ('qwerty'):     1.0395500409649685
# Кнут-Морріс-Пратт ('qwerty'): 1.2972526249941438
# Рабін-Карп ('qwerty'):        7.929367499891669
# Висновки:

# Для статті 1 найшвидшим алгоритмом для підрядка "алгоритм" виявився алгоритм Бойєра-Мура, а для підрядка "qwerty" також алгоритм Бойєра-Мура.
# Для статті 2 аналогічні результати. Тому алгоритм Бойєра-Мура продемонстрував найвищу ефективність для цих вхідних даних.
# Алгоритм Рабіна-Карпа виявився найповільнішим для всіх випадків.
# Загалом, алгоритми Бойєра-Мура та Кнута-Морріса-Пратта показали порівнянно високу продуктивність для пошуку підрядків у наданих текстах.

# Для зчитування тексту з посиланих файлів з Google Drive, вам потрібно імпортувати та використати сторонній модуль для взаємодії з Google Drive API. Одним з таких модулів є PyDrive.
# Встановити PyDrive можна через pip:
# Copy codepip install pydrive
# Потім ви повинні налаштувати доступ PyDrive до вашого облікового запису Google. Для цього слід виконати наступні кроки:

# Відвідайте Python Quickstart (https://developers.google.com/drive/api/v3/about-auth) та виберіть "Desktop app".
# На наступній сторінці натисніть "Enable the Drive API".
# Виберіть "Download Client Configuration" та збережіть json-файл.
# Встановіть шлях до збереженого файлу у змінне settings.yaml після того, як авторизуєтесь.

# Після налаштування доступу, змініть код для зчитування текстів з посиланих файлів:
# pythonCopy codefrom pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive

# # Авторизація
# gauth = GoogleAuth()
# drive = GoogleDrive(gauth)

# # Завантаження файлів зі статтями
# file1 = drive.CreateFile({'id': '18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh'})
# file1.GetContentFile('article1.txt')
# with open('article1.txt', 'r', encoding='utf-8') as f:
#     text1 = f.read()

# file2 = drive.CreateFile({'id': '13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ'}) 
# file2.GetContentFile('article2.txt')
# with open('article2.txt', 'r', encoding='utf-8') as f:
#     text2 = f.read()

# # ... решта коду ...
# Цей код автентифікується в Google API, завантажує файли за посиланнями в поточну директорію, а потім зчитує їх вміст у рядки text1 та text2 відповідно.
# Зверніть увагу, що при першому запуску вам буде запропоновано пройти авторизацію через веб-браузер та надати дозвіл додатку на доступ до Google Drive.
# Після успішної авторизації код зможе отримати доступ до файлів з наданими посиланнями і ви зможете використовувати змінні text1 та text2 для подальшої обробки.