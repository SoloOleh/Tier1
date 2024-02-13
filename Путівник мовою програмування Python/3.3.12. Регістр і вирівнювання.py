# >>> setup = 'beetles buzzing over cherries...'
# >>> setup.strip('.')
# 'beetles buzzing over cherries'
# >>> setup
# 'beetles buzzing over cherries...'
# >>> setup.title()
# 'Beetles Buzzing Over Cherries...'
# >> setup.capitalize()
# 'Beetles buzzing over cherries...'
# >>> setup.upper()
# 'BEETLES BUZZING OVER CHERRIES...'
# >>> setup.lower()
# 'beetles buzzing over cherries...'

setup = 'Beetles buzzing over Cherries...'
# >>> setup.swapcase()
# 'bEETLES BUZZING OVER cHERRIES...'
# >>> setup.center(40)
# '    beetles buzzing over cherries...    '
# >>> setup.ljust(40)
'beetles buzzing over cherries...        '
test = setup.rjust(40)
# '        beetles buzzing over cherries...'
print (test)