planets = ['Mercury', 'Jupiter', 'Earth', 'Mars', 'Venus']

test = planets.append('Uranus')
print(planets) # ['Mercury', 'Jupiter', 'Earth', 'Mars', 'Venus', 'Uranus']

planets.insert(3, 'Neptune')
print(planets) #['Mercury', 'Jupiter', 'Earth', 'Neptune', 'Mars', 'Venus', 'Uranus']

planets.insert(10, 'Unknown planet')
print(planets) #['Mercury', 'Jupiter', 'Earth', 'Neptune', 'Mars', 'Venus', 'Uranus', 'Unknown planet']