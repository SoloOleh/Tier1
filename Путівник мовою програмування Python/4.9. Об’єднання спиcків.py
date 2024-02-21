planets = ['Earth', 'Mars']
satellites = ['Moon', 'Deimos', 'Phobos']
planets.extend(satellites) # або planets += satellites
print (planets) #['Earth', 'Mars', 'Moon', 'Deimos', 'Phobos']

planets = ['Earth', 'Mars']
satellites = ['Moon', 'Deimos', 'Phobos']
planets.append(satellites)
print (planets) # ['Earth', 'Mars', ['Moon', 'Deimos', 'Phobos']]