>>> del  languages_programmers['Swift']
>>> languages_programmers
{'Scala': 'Martin Odersky', 'JavaSript': 'Brendan Eich', 'Python': 'Guido van Rossum', 'PHP': 'Rasmus Lerdorf', 'Ruby': 'Yukihiro Matsumoto', 'C': 'Dennis Ritchie', 'C++': 'Bjarne Stroustrup'}
>>> del  languages_programmers['C++']
>>> languages_programmers
{'Scala': 'Martin Odersky', 'JavaSript': 'Brendan Eich', 'Python': 'Guido van Rossum', 'PHP': 'Rasmus Lerdorf', 'Ruby': 'Yukihiro Matsumoto', 'C': 'Dennis Ritchie'}


>>> languages_programmers.clear()
>>> languages_programmers
{}

>>> languages_programmers = {}
>>> languages_programmers
{}