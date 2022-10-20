class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
        self.mass = 25
        self.thickness = 0.05

    def calculateМass(self):
        print(self.__length * self.__width * self.mass * self.thickness)



road = Road(20,5000)
road.calculateМass()