planets = ['Mercury', 'Jupiter', 'Earth', 'Mars', 'Venus']

a = planets[0:3]
print(a) #['Mercury', 'Jupiter', 'Earth']

b = planets[::2]
print(b) #['Mercury', 'Earth', 'Venus']

c = planets[::-3]
print(c) #['Venus', 'Jupiter']

d = planets[::-1] # розміщення елементів списку у зворотному порядку
print(d) #['Venus', 'Mars', 'Earth', 'Jupiter', 'Mercury']