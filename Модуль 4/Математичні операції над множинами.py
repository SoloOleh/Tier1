a = set('hello')
print(a)    # {'e', 'h', 'l', 'o'}

b = set('hi there!')
print(b)    # {'r', ' ', 'i', 'e', '!', 'h', 't'}

a & b   # {'e', 'h'} # Щоб знайти загальні елементи для двох множин, виконаємо над ними операцію & (AND)
a ^ b   # {' ', '!', 'i', 'l', 'o', 'r', 't'} # Знайдемо усі елементи з двох множин, окрім загальних, за допомогою оператора ^ (XOR)
a | b   # {' ', '!', 'e', 'h', 'i', 'l', 'o', 'r', 't'} #Об'єднання множин, або просто усі елементи з обох множин знаходяться за допомогою оператора | (OR):
