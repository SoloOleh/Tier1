def normal_name(list_name):
    def capitalize_name(name):
        return name.capitalize()

    return list(map(capitalize_name, list_name))

# Тестування функції
name = ["dan", "jane", "steve", "mike"]
print(normal_name(name))  # Виведе ['Dan', 'Jane', 'Steve', 'Mike']

#або з лямбдою
def normal_name(list_name):
    return list(map(lambda name: name.capitalize(), list_name))

# Тестування функції
name = ["dan", "jane", "steve", "mike"]
print(normal_name(name))  # Виведе ['Dan', 'Jane', 'Steve', 'Mike']


