while True:
    num = int(input("Введіть число (0 для виходу): "))
    if num == 0:
        break
    repeat = int(input("Скільки разів помножити число на 2? "))
    for i in range(repeat):
        num = num * 2
    print(num)
    print (i)
