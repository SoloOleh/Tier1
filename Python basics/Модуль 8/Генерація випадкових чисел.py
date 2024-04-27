# import random
# print (random.randint(1, 1000))

# import random
# a = random.random()
# print (a)

import random
fruits = ['apple', 'banana', 'orange']
random.shuffle(fruits) # перемішує незвороньо
print(fruits)   # ['banana', 'orange', 'apple']


import random
fruits = ['apple', 'banana', 'orange']
a = random.choice(fruits)
print(a)   # 'banana' 

import random
fruits = ['apple', 'banana', 'orange']
print(random.choices(fruits, k=4))   # ['banana', 'orange', 'orange', 'orange']

import random
fruits = ['apple', 'banana', 'orange'] #вибрати N елементів, що не повторюються, зі списку:
print(random.sample(fruits, k=2))   # ['banana', 'orange']

