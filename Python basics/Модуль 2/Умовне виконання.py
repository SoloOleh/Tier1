name = input("What is your name? ")
print(f"Hello {name}")

age = input("How old are you? ")
if int(age) >= 18:
    print("You are adult already.")
else:
    print("You are infant yet.")

number = input('Введіть число ')
a = int(number)
if a > 0:
    print('Число додатне')
elif a < 0:
    print("Число від'ємне")
else:
    print('Це число - нуль')

number = input('Введіть число')
a = int(number)
if a > 0:
    print('Число додатне')
elif a == 1:
    print('Число дорівнює 1') #В такому випадку код для умови a == 1 ніколи не виконається.
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
