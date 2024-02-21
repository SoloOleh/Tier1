languages_programmers = {
'JavaSript': 'Brendan Eich', 
'Python': 'Guido van Rossum', 
'Ruby': 'Yukihiro Matsumoto', 
'PHP': 'Rasmus Lerdorf',
'Scala': 'Martin Odersky'
}
print (languages_programmers)
# {'Python': 'Guido van Rossum', 'Scala': 'Martin Odersky', 'Ruby': 'Yukihiro Matsumoto', 'PHP': 'Rasmus Lerdorf', 'JavaSript': 'Brendan Eich'}

languages_programmers['C'] = 'Dennis MacAlistair Ritchie'
print (languages_programmers)
# {'Scala': 'Martin Odersky', 'JavaSript': 'Brendan Eich', 'Python': 'Guido van Rossum', 'PHP': 'Rasmus Lerdorf', 'Ruby': 'Yukihiro Matsumoto', 'C': 'Dennis MacAlistair Ritchie'}

languages_programmers['C'] = 'Dennis Ritchie'
print (languages_programmers) #{'Scala': 'Martin Odersky', 'JavaSript': 'Brendan Eich', 'Python': 'Guido van Rossum', 'PHP': 'Rasmus Lerdorf', 'Ruby': 'Yukihiro Matsumoto', 'C': 'Dennis Ritchie'}

languages_programmers = {
'JavaSript': 'Brendan Eich',
'Python': 'Guido van Rossum',
'C': 'Dennis MacAlistair Ritchie',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
'Scala': 'Martin Odersky',
'C': 'Dennis Ritchie'
}
print (languages_programmers)#{'PHP': 'Rasmus Lerdorf', 'Scala': 'Martin Odersky', 'JavaSript': 'Brendan Eich', 'Python': 'Guido van Rossum', 'C': 'Dennis Ritchie', 'Ruby': 'Yukihiro Matsumoto'}