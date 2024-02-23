num = int(input("Enter the integer (0 to 100): "))
sum = 0
i = 1
while i <= num:
    sum += i
    i += 1

print(f"Сума чисел від 1 до {num} включно: {sum}")