# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y
    
#     @property
#     def x(self):
#         return self.__x
    
#     @x.setter
#     def x(self, x):
#         if type(x) is int or type(x) is float:
#             self.__x = x
#         else:
#             self.__x = None
    
#     @property
#     def y(self):
#         return self.__y
    
#     @y.setter
#     def y(self, y):
#         if type(y) is int or type(y) is float:
#             self.__y = y
#         else:
#             self.__x = None

# point = Point("a", 10)

# print(point.x)  # None
# print(point.y)  # 10

# point = Point(10, "s")
# print(point.x)  
# print(point.y)  


class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is int or type(x) is float:
            self.__x = x
        else:
            print("Warning: x value must be numeric.")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is int or type(y) is float:
            self.__y = y
        else:
            print("Warning: y value must be numeric.")

point = Point("a", 10)

print(point.x)  # None
print(point.y)  # 10


point = Point(10, "s")
print(point.x)  
print(point.y)  