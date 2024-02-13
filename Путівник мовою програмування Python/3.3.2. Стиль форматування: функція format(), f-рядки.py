# n = 25
# f = 9.03
# s = 'search string'

# '{} {} {}'.format(n, f, s) #'25 9.03 search string'
# print (n, f, s)

# '{2} {0} {1}'.format(n, f, s) #'search string 25 9.03'
# print (n, f, s)

# '{0:d} {1:f} {2:s}'.format(n, f, s) #'25 7.030000 search string'
# print (n, f, s)

# '{0:10d} {1:10f} {2:10s}'.format(n, f, s)
# #'        25   9.030000 search string'

# >>> '{0:<15d} {1:<15f} {2:<15s}'.format(n, f, s)
# '25              9.030000        search string  '

# >>> '{0:=^21s}'.format('My web-page')
# '=====My web-page====='

# >>> price = 250.67890
# >>> f'your account: {price:.3f}'
# 'your account: 250.679'
print('Languages:\nPython\nC\nRuby')
print('ascii\tdoctor')
print("The language \"Python\" is named after Monty Python, not the snake.")
