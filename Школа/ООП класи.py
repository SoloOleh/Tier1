class Dog:
    #pass
    name = None
    age = None
    isHappy = None

    def set_data(self, dog_name, age, isHappy):
        self.name = dog_name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        print(self.name, "age:", self.age, ". Happy: ", self.isHappy)
        print (f'{self.name}, age: {self.age}, Happy: {self.isHappy}')


dog1 = Dog()
# dog1.name = 'Scoobby'
# dog1.age = 3
# dog1.isHappy = True

# або 
dog1.set_data('Scoobby', 3, True)

dog2 = Dog()
dog2.name = 'Bob'
dog2.age = 5
dog2.isHappy = False

# print(dog1.name)
# print(dog2.name)
# або 
dog1.get_data()
dog2.get_data()
