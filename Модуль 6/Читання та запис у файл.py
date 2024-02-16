# fh = open('Модуль 6/test.txt', 'w+')
# fh.write('hello!')
# fh.seek(0)
# first_two_symbols = fh.read()
# print(first_two_symbols)  # 'he'
# fh.close()

# fh = open('Модуль 6/test.txt', 'w')
# fh.write('hello!')
# fh.close()

# fh = open('Модуль 6/test.txt', 'r')
# all_file = fh.read()
# print(all_file)  # 'hello!'
# fh.close()

# fh = open('Модуль 6/test.txt', 'w')
# fh.write('hello!')
# fh.close()
# fh = open('Модуль 6/test.txt', 'r')
# while True:
#     symbol = fh.read(1)
#     if len(symbol) == 0:
#         break
#     print(symbol)
# fh.close()

# fh = open('Модуль 6/test.txt', 'w')
# fh.write('first line\nsecond line\nthird line')
# fh.close()
# fh = open('Модуль 6/test.txt', 'r')
# while True:
#     line = fh.readline()
#     if not line:
#         break
#     print(line) 
# fh.close()

fh = open('Модуль 6/test.txt', 'w')
fh.write('first line\nsecond line\nthird line')
fh.close()
fh = open('Модуль 6/test.txt', 'r')
lines = fh.readlines()
print(lines) #['first line\n', 'second line\n', 'third line']
fh.close()


