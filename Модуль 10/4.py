class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    def change_color(self, color):
        Animal.color = color
    
    # def change_color(self, new_color):
    #     Animal.color = new_color


first_animal = Animal("Buddy", 10)
second_animal = Animal("Charlie", 12)
first_animal.change_color("red")
second_animal.change_color("red")