import time

class TrafficLight:
    def __init__(self):
        self.__color = "Red"


    def running(self):
        match self.__color:
            case "Red":
                print(self.__color)
                time.sleep(7)
                self.__color = "Yellow"

            case "Yellow":
                print(self.__color)
                time.sleep(2)
                self.__color = "Green"

            case "Green":
                print(self.__color)
                time.sleep(5)
                self.__color = "Red"



trafficLight = TrafficLight()
while True:
    trafficLight.running()