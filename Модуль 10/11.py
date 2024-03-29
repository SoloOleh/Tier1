class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def say(self):
        return "Meow"


class CatDog:
    def __init__(self, nickname, weight):
        self.cat = Cat(nickname, weight)

    def say(self):
        return self.cat.say()

    def change_weight(self, weight):
        self.cat.change_weight(weight)

# Приклад використання:
catdog = CatDog("Fluffy", 5)
print(catdog.say())  # Виведе: Meow
catdog.change_weight(6)
print(catdog.say())  # Виведе: Meow
