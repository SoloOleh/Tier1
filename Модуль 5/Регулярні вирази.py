import re

s = "I am 25 years old"
age = re.search('\d+', s)
print(age)  # <re.Match object; span=(5, 7), match='25'>

s = "I am 25 years old."
age = re.search('\d+', s)
print(age.group())  # 25

s = "I bought 7 nuts for 6$ and 10 bolts for 3$."
numbers = re.findall('\d+', s)
print(numbers)  # ['7', '6', '10', '3']

p = re.sub(r'(blue|white|red)', 'colour', 'blue socks and red shoes')
print(p)    # colour socks and colour shoes

