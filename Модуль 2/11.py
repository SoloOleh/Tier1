"""
Досить часто програмісти стикаються із завданнями кодування інформації. Закодувати повідомлення в чаті між двома користувачами. Зашифрувати пароль та ім'я користувача при автентифікації користувача через мережу і т.і.

Напишіть програму, що реалізує код Цезаря. Він названий на честь великого римського імператора Юлія Цезаря.

Ідея шифрування полягає у циклічному зміщенні букв на задану кількість. Наприклад, якщо зміщення на три позиції, то літера A стає літерою D, B – E тощо. Останні три літери алфавіту зациклюються та переносяться на початок. Літера X стає A, Y – B, а Z – C. Цифри, пробіли та інші символи не шифруються.

У програмі користувач вводить фразу та число для зсуву, після чого треба вирахувати нове закодоване повідомлення.

Програма шифруватиме як малі (a-z), так і великі літери (A-Z).

Для розв'язку цього завдання знадобиться знання двох нових функцій. Перша функція ord. Вона перетворює символ на число, яке є позицією в таблиці ASCII.

ord("a")  # 97
Можна вважати, що отриманий результат '97' — це числове представлення символу a для комп'ютера.

Зворотна функція chr повертає рядковий символ у таблиці ASCII за позицією, переданою як аргумент.

chr(118)  # 'v'
Детальніший принцип шифрування.

Розглянемо для прикладу як зашифрувати символ v. Щоб отримати позицію символу v щодо початкового символу a, необхідно виконати вираз

pos = ord('v') - ord('a')  # 21
Але, згідно з алгоритмом, нам необхідно враховувати зсув, який може бути довільним, наприклад, 33. І пам'ятати, що алфавіт англійської мови заснований на латинському алфавіті та складається з 26 літер. Тому кінцева позиція символу v щодо символу a для шифрування з урахуванням цього — дорівнює 2.

pos = ord('v') - ord('a')  # 21
pos = (pos + 33) % 26  # 2
Залишився останній крок, отримати новий символ:

pos = ord('v') - ord('a')  # 21
pos = (pos + 33) % 26  # 2
new_char = chr(pos + ord("a"))  # 'c'
Символ v зі зміщенням 33 шифрується символом c.

Тести перевіряють та кодують наступні рядки:

"Hello my little friends!", offset = 37,
"Hello world!", offset = 7
"""
message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    if ch.isalpha():
        if ch.islower():
            start_char = ord('a')
        else:
            start_char = ord('A')
        new_code = (ord(ch) - start_char + offset) % 26 + start_char
        new_char = chr(new_code)
        encoded_message += new_char
    else:
        encoded_message += ch  