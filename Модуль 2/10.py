sum = 0
while True:
  num = int(input("Введіть ціле число (0 для виходу): "))
  if num == 0:
    break

  for i in range(num + 1):
    if i % 2 == 0:
      sum += i
"""
sum = 0
while True:
    num = int(input("Enter integer (0 for output): "))
    if num == 0:
        break
    for i in range(num + 1):
        if
            
        sum = sum + i
"""
мій варіант
sum = 0
while True:
    num = int(input("Enter integer (0 for output): "))
    if num == 0:
        break
    for i in range(num + 1):
        if i % 2 == 1:
            continue
        sum = sum + i