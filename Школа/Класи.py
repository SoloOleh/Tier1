class Build:
    __year = None
    __city = None
    
    def __init__(self, year, city):
        self.year = year
        self.city = city
        
    def get_info(self):
        print ("Year: ", self.year, ". City: ", self.city, sep='')

class School(Build):
    __pupils = None

    def __init__(self, year, city, pupils=500):
        super(School, self).__init__(year, city)
        self.pupils = pupils
    
    def get_info(self):
        super().get_info()
        print("Pupils:", self.pupils)

class House(Build):
    pass
class Shop(Build):
    pass
    
school = School(1990, 'Seatle', 700)
school.__pupils = 500
school.get_info()
house = Build(2010, 'New york')
house.get_info()
shop = Build(2000, 'Miami')
