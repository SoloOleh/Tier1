periodic_table = {'Hydrogen': 1, 'Helium': 2} 
print(periodic_table) 

carbon = periodic_table.setdefault('Ferrum', 26) 
print(periodic_table) 
print(carbon) 

periodic_table = {'Hydrogen': 1, 'Helium': 2}
helium = periodic_table.setdefault('Helium', 101)
print(periodic_table)
print(helium)