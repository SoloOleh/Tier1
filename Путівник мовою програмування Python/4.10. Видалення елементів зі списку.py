# planets = ['Mercury', 'Jupiter', 'Earth', 'Mars', 'Venus']
# del planets[-1]
# print (planets) ['Mercury', 'Jupiter', 'Earth', 'Mars']

# >>> planets = ['Mercury', 'Jupiter', 'Earth', 'Mars', 'Venus']
# >>> planets[3]
# 'Mars'
# >>> del planets[3]
# >>> planets
# ['Mercury', 'Jupiter', 'Earth', 'Venus']
# >>> planets[3]
# 'Venus'
# >>>

# planets = ['Mercury', 'Jupiter', 'Earth', 'Mars', 'Venus']
# planets.remove('Jupiter')
# print (planets) #['Mercury', 'Earth', 'Mars', 'Venus']

planets = ['Mercury', 'Jupiter', 'Earth', 'Mars', 'Venus']
a = planets.pop() #'Venus'
print (a)
print (planets) #['Mercury', 'Jupiter', 'Earth', 'Mars']
b = planets.pop(1) #'Jupiter'
print (b)
print (planets) #['Mercury', 'Earth', 'Mars']