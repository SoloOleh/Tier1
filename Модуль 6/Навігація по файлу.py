# fh = open('Модуль 6/test.txt', 'w+')
# fh.write('hello!')
# fh.seek(1)
# second = fh.read(1)
# print(second)  # 'e'
# fh.close()

fh = open('Модуль 6/test.txt', 'w+')
fh.write('hello!')

position = fh.tell()
print(position) # 6

fh.seek(1)
position = fh.tell()
print(position) # 1

fh.read(2)
position = fh.tell()
print(position) # 3
fh.close()

