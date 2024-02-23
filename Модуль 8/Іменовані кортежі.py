person = ('Mick', 'Nitch', 35, 'Boston', '01146')

import collections
Person = collections.namedtuple('Person', ['name', 'last_name', 'age', 'birth_place', 'post_index'])
person = Person('Mick', 'Nitch', '35', 'Boston', '01146')
person.name         # 'Mick'
person.post_index   # '01146'
person.age          # 35
person[3]           # 'Boston'

