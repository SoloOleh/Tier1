class Dog:
    #pass
    name = None
    age = None
    isHappy = None

    # def __init__(self):
    #     print ('Object is created')
    
    def __init__(self, name='Gav', age=(1,2), isHappy=3):
        print ('Object is created')
        self.set_data(name, age, isHappy)
        self.get_data()
    

    def set_data(self, dog_name, age=1, isHappy=True):
        self.name = dog_name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        print(self.name, "age:", self.age, ". Happy: ", self.isHappy)
        print (f'{self.name}, age: {self.age}, Happy: {self.isHappy}')


dog1 = Dog('Alex')
#dog1.set_data('Alex', 5)
dog2 = Dog('Bob', 5, False)




