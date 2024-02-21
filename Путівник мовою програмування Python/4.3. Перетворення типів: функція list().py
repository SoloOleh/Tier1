test = list('sun') 
print (test) #['s', 'u', 'n']

mybirthday = '3/4/1981'
test2 = mybirthday.split('/')
print (test2) #['3', '4', '1981']

result = 'a|b||c|d|||e'
test3 = result.split('|')
print (test3) #['a', 'b', '', 'c', 'd', '', '', 'e']

result2 = ['a', 'b', 'c', 'd', 'e']
test4 = ', '.join(result2)
print (test4)