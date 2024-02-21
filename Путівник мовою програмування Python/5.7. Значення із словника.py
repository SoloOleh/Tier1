>>> languages_programmers = {'JavaSript': 'Brendan Eich', 'Python': 'Guido van Rossum', 'Ruby': 'Yukihiro Matsumoto'}

>>> languages_programmers['Ruby']
'Yukihiro Matsumoto'

>>> languages_programmers['PHP']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'PHP'

>>> languages_programmers.get('Ruby')
'Yukihiro Matsumoto'
>>> languages_programmers.get('PHP', 'PHP not in dictionary.')
'PHP not in dictionary.'