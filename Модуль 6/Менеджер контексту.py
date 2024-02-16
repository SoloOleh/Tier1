fh = open('Модуль 6/test.txt')
try:
    some_useful_function(fh)
finally:
    fh.close()

with open('Модуль 6/test.txt', 'w+') as fh:
    some_useful_function(fh)
