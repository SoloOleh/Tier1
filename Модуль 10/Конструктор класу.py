class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        return f"Hi {self.name}"


p = Person("Boris", 34)
print(p.name)  # Boris
print(p.age)  # 34
print(p.greeting())  # Hi Boris
