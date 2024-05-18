import timeit

def boyer_moore_search(text, pattern):
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

def kmp_search(main_string, pattern):
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

def rabin_karp_search(main_string, substring):
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

with open("/Users/solo/Desktop/IT/Repository/Tier1/стаття 1.txt", "r", encoding="iso-8859-1") as f:
    text1 = f.read()

with open("/Users/solo/Desktop/IT/Repository/Tier1/стаття 2.txt", "r", encoding="iso-8859-1") as f:
    text2 = f.read()

article1 = text1
article2 = text2

real_substring = "алгоритм"
fake_substring = "qwerty"

# Функція для заміру часу
def time_algorithm(algorithm, text, substring):
    setup_code = f"from __main__ import {algorithm}, text, substring"
    test_code = f"{algorithm}(text, substring)"
    times = timeit.repeat(setup=setup_code, stmt=test_code, repeat=3, number=100)
    return min(times)

# Виведення результатів
results = {}
for text_name, text in [("Стаття 1", article1), ("Стаття 2", article2)]:
    for substring, substring_name in [(real_substring, "Real"), (fake_substring, "Fake")]:
        for algorithm in ["boyer_moore_search", "kmp_search", "rabin_karp_search"]:
            time_taken = time_algorithm(algorithm, text, substring)
            results[(text_name, substring_name, algorithm)] = time_taken

for key, time in results.items():
    print(f"Text: {key[0]}, Substring: {key[1]}, Algorithm: {key[2]}, Time: {time:.6f} seconds")


# Висновки про швидкість алгоритмів

## Стаття 1

**Текст "Стаття 1"**

- **Бойєр-Мур:**
  - Шаблон 'алгоритм': x сек
  - Шаблон 'abcdefghijk': x сек

- **Кнут-Морріс-Пратт:**
  - Шаблон 'алгоритм': x сек
  - Шаблон 'abcdefghijk': x сек

- **Рабін-Карп:**
  - Шаблон 'алгоритм': x сек
  - Шаблон 'abcdefghijk': x сек

## Стаття 2

**Текст "Стаття 2"**

- **Бойєр-Мур:**
  - Шаблон 'алгоритм': x сек
  - Шаблон 'abcdefghijk': x сек

- **Кнут-Морріс-Пратт:**
  - Шаблон 'алгоритм': x сек
  - Шаблон 'abcdefghijk': x сек

- **Рабін-Карп:**
  - Шаблон 'алгоритм': x сек
  - Шаблон 'abcdefghijk': x сек

## Загальний висновок

- **Алгоритм Бойєра-Мура** зазвичай показує кращі результати для коротких шаблонів у довгих текстах через свої оптимізації при зміщеннях.
- **Кнут-Морріс-Пратт** ефективний для шаблонів з повторюваними патернами, оскільки використовує часткові збіги.
- **Рабін-Карп** виявився корисним у сценаріях з множинними входженнями одного шаблону в текст через використання хешування.