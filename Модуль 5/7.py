# print('dec: {:d} hex: {:x} bin: {:b}'.format(15, 15, 15))  # dec: 15 hex: f bin: 1111

# print('pi: {:0.3}'.format(3.1415))  # pi: 3.14

# print('"{}" "{:+}" "{:-}" "{: }"'.format(1, 2, -3, 4))  # "1" "+2" "-3" " 4"

# print("|{:<10}|{:*^10}|{:>10}|".format('left', 'center', 'right'))  # |left      |**center**|     right|


def formatted_numbers():
    # Header with central alignment and no extra spaces around |
    header = f"|{'decimal':^10}|{'hex':^10}|{'binary':^10}|"
    lines = [header]
    
    # Generating table rows without extra spaces around |
    for i in range(16):
        decimal = f"{i:<10}"  # Decimal left aligned
        hex_num = f"{i:^10x}"  # Hexadecimal centered
        binary = f"{i:>10b}"  # Binary right aligned
        line = f"|{decimal}|{hex_num}|{binary}|"
        lines.append(line)
    
    return lines

# Usage example
for el in formatted_numbers():
    print(el)









