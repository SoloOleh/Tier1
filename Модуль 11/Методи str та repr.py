class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point ({self.x}, {self.y})'


a = Point(1, 9)


class Human:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Hello! I am {self.name}'


# bill = Human('Bill')
# bill_str = str(bill)
# print(bill_str)  # Hello! I am Bill

cat = Human(name="Myron", age = 20)
cat.__str__()