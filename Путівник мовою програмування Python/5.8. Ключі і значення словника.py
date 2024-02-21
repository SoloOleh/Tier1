light_signals = {'green': 'go', 'yellow': 'get ready', 'red': 'stop'}

a = light_signals.keys()
print (a) #dict_keys(['green', 'yellow', 'red'])

b = list(light_signals.keys())
print (b)

c = list(light_signals.values())
print (c)

d = list(light_signals.items())
print (d)