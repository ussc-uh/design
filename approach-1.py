
from abc import ABC, abstractmethod

# interface Vehicle
class Vehicle(ABC):

    @abstractmethod
    def drive(self, dist: int):
        pass

    @abstractmethod
    def getDistance(self):
        pass


# Class Car inherits (implements) the interface Vehicle
class Car(Vehicle):
    def __init__(self, initdistance: int):
        self.distance = initdistance

    def drive(self, dist: int):
        print("driving a Car...")
        self.distance += dist

    def getDistance(self):
        return self.distance


# Class SportsCar inherits the class Car
class SportsCar(Car):
    def __init__(self, initdistance: int):
        super().__init__(initdistance)

    def drive(self, dist: int):
        print("driving a sports car...")
        super().drive(dist)


# main Program
def useVehicle(vehcle: Vehicle):
    vehcle.drive(10)
    print(vehcle.getDistance())

car1: Car = Car(0)
spcar1: SportsCar = SportsCar(0)
listVehicle = [car1, spcar1]

for vehicle in listVehicle:
    useVehicle(vehicle)

# output-->:
# driving a Car...
# 10
# driving a sports car...
# driving a Car...
# 10
