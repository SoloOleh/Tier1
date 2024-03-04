class Animal:
    def __init__(self, nickname, is_vaccinated):
        self.nickname = nickname
        self.is_vaccinated = is_vaccinated

    def get_info(self):
        return f"It's animal. His name is {self.nickname} and vaccinated: {self.is_vaccinated}"

class Cat(Animal):
    def __init__(self, nickname, is_vaccinated, color = "Black"):
        super().__init__(nickname, is_vaccinated)
        # супер замінює рядки нижче
        # self.nickname = nickname
        # self.is_vaccinated = is_vaccinated
        self.color = color

    def get_info(self):
        base_info = super().get_info()
        print(base_info + f" color: {self.color}")

class Dog(Animal):
    pass
              

# animal = Animal("Simon", 4)
# print(animal.nickname)
# animal.age = 5
# print(animal.get_info())

cat = Cat(nickname="Myron", is_vaccinated=True, color="Red")
cat.get_info()

dog = Dog("Rex", True)
print(dog.get_info())