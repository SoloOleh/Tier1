import math

a = float(input('Enter side A '))
b = float(input('Enter side B '))
c = float(input('Enter side C '))
# або замість нагромадження написати a = float(a)
# p is half of perimeter and P is a perimeter
"""
ще так може виглядати 
коментар в кілька
рядків
"""
# a = round(a, 2) заокруглення 
# res = round(S, 2)
P = a + b + c
p = P / 2
S = math.sqrt(p * (p-a)*(p-b)*(p-c))


print (type(a))
print (a, b, c)
print ("The square is", S)