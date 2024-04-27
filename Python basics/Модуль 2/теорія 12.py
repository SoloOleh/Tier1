try:
    num = int(input("Введіть розмір команди: "))
    award = 10000
    bonus_for_person = award / num
except ValueError:
    print("Ви ввели не число!")
except ZeroDivisionError:
    print("Ви ввели нуль учасників!")
else:
    print(f"Нагорода кожному учаснику {bonus_for_person} золота!")
finally:
    print("До побачення!")