languages_programmers = {
'JavaSript': 'Brendan Eich',
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
'Scala': 'Martin Odersky',
'C': 'Dennis Ritchie'
}
others = {'C++': 'Bjarne Stroustrup', 'Swift': 'Chris Lattner'}
languages_programmers.update(others)
print (languages_programmers)



first = {'a': 10, 'b': 20}
second = {'b': 'other'}
first.update(second)
print (first) #{'a': 10, 'b': 'other'}