# Class Car
class Car():
    def __init__(self, initdistance: int):
        self.distance = initdistance

    def drive(self, dist: int):
        print("driving a Car...")
        self.distance += dist

    def getDistance(self):
        return self.distance


# Class SportsCar [Very similar to Car]
class SportsCar():
    def __init__(self, initdistance: int):
        self.distance = initdistance

    def drive(self, dist: int):
        print("driving a sports car...")
        self.distance += dist
    
    def getDistance(self):
        return self.distance


# main Program
def useVehicle(vehicle):
    vehicle.drive(10)
    print(vehicle.getDistance())

car1 = Car(0)
spcar1 = SportsCar(0)
listVehicle = [car1, spcar1]

for vehicle in listVehicle:
    useVehicle(vehicle)

# output-->:
# driving a Car...
# 10
# driving a sports car...
# 10
