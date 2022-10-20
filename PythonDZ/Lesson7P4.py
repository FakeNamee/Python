class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("car is going")

    def stop(self):
        print("car stoped")

    def turn(self, direction):
        print("car turned %s" % direction)

    def show_speed(self):
        print("car speed is = %s" % self.speed)


class TownCar(Car):
    def __init__(self,speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print("car speed is = %s \n Lower the speed!" % self.speed)
        else:
            print("car speed is = %s" % self.speed)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print("car speed is =%s \n Lower the speed!" % self.speed)
        else:
            print("car speed is = %s" % self.speed)


car = TownCar(61, "black", "name", True)
car.turn("left")
car.go()
car.stop()
car.show_speed()

print()

car = WorkCar(41, "black", "name", True)
car.turn("left")
car.go()
car.stop()
car.show_speed()