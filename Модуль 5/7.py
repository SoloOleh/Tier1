# print('dec: {:d} hex: {:x} bin: {:b}'.format(15, 15, 15))  # dec: 15 hex: f bin: 1111

# print('pi: {:0.3}'.format(3.1415))  # pi: 3.14

# print('"{}" "{:+}" "{:-}" "{: }"'.format(1, 2, -3, 4))  # "1" "+2" "-3" " 4"

# print("|{:<10}|{:*^10}|{:>10}|".format('left', 'center', 'right'))  # |left      |**center**|     right|


# def formatted_numbers():
#     header = f"|{'decimal':^10}|{'hex':^10}|{'binary':^10}|"
#     rows = [header]
#     for i in range(16):
#         decimal = f"{i:<10}"  # Left align
#         hexa = f"{i:^10X}"    # Center align and uppercase hexadecimal
#         binary = f"{i:>10b}"  # Right align and binary format
#         row = f"|{decimal}|{hexa}|{binary}|"
#         rows.append(row)
#     return rows

# # Print the formatted table without divider
# for el in formatted_numbers():
#     print(el)

# def formatted_numbers():
#     header = f"|{'decimal':^10}|{'hex':^10}|{'binary':^10}|"
#     rows = [header]
#     for i in range(16):
#         decimal = f"{i:<10}"  # Left align
#         hexa = f"{i:^10X}"    # Center align and uppercase hexadecimal
#         binary = f"{i:>10b}"  # Right align and binary format
#         row = f"|{decimal}|{hexa}|{binary}|"
#         rows.append(row)
#     return rows

# Print the formatted table without divider
# for el in formatted_numbers():
#     print(el)

# def formatted_numbers():
#   """
#   Функція повертає список відформатованих рядків для таблиці чисел.

#   Args:
#       None

#   Returns:
#       Список рядків.
#   """

#   table = []
#   # Заголовки таблиці
#   table.append("| {:^10} | {:^10} | {:^10} |".format("decimal", "hex", "binary"))
#   # Цикл для перебору чисел від 0 до 15
#   for i in range(16):
#     # Форматування десяткового числа
#     decimal = f"{i:10}"
#     # Форматування шістнадцяткового числа
#     hexadecimal = f"{i:02x}".upper()
#     # Форматування двійкового числа
#     binary = f"{i:08b}"
#     # Додавання рядка до таблиці
#     table.append("| {:10} | {:^10} | {:>10} |".format(decimal, hexadecimal, binary))
#   return table

# # Виведення таблиці
# for el in formatted_numbers():
#     print(el)

# def formatted_numbers():
#     # Header with central alignment
#     header = f"| {'decimal':^10} | {'hex':^10} | {'binary':^10} |"
#     lines = [header]
    
#     # Generating table rows
#     for i in range(16):
#         decimal = f"{i:<10}"  # Decimal left aligned
#         hex_num = f"{i:^10x}"  # Hexadecimal centered
#         binary = f"{i:>10b}"  # Binary right aligned
#         line = f"| {decimal} | {hex_num} | {binary} |"
#         lines.append(line)
    
#     return lines

# # Let's test the function by printing its output
# for el in formatted_numbers():
#     print(el)








