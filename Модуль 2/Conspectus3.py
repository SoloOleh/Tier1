a = input('Введіть число')
a = int(a)
if a > 0:
    print('Число додатне')
elif a == 1: #В такому випадку код для умови a == 1 ніколи не виконається.
    print('Число дорівнює 1')
else:
    print("a <= 0")

# google bard variant 
#a = input('Введіть число')
#a = int(a)
#if a > 1:
#    print('Число додатне')
#elif a == 1:
#    print('Число дорівнює 1')
#elif a == 0:
#    print('Число дорівнює 0')
#else:
#    print("a <= 0")