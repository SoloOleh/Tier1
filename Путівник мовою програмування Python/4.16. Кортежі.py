# >>> empty_tuple = ()
# >>> empty_tuple
# ()

# сurrency_units = 'pound',
# print (сurrency_units) #('pound',)
# сurrency_units = 'pound', 'dollar', 'euro'
# print (сurrency_units) #('pound', 'dollar', 'euro')

# >>> сurrency_units = 'pound', 'dollar', 'euro'
# >>> p, d, e = сurrency_units
# >>> p
# 'pound'
# >>> d
# 'dollar'
# >>> e
# 'euro'

# >>> network_name = 'netis'
# >>> password = 'pass12345'
# >>> network_name, password = password, network_name
# >>> network_name
# 'pass12345'
# >>> password
# 'netis'

сurrency_units = ['pound', 'dollar', 'euro']
tuple(сurrency_units)
print (сurrency_units)#['pound', 'dollar', 'euro']


сurrency_units = ['pound', 'dollar', 'euro']
a = tuple(сurrency_units)
print (a)#('pound', 'dollar', 'euro')
