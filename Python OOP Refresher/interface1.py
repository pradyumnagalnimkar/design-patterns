from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        return "The car is driving."


class Bicycle(Vehicle):
    def move(self):
        return "The bicycle is pedalling."


class Boat(Vehicle):
    def move(self):
        return "The boat is sailing."


def start_vehicle(vehicle):
    print(vehicle.move())


car = Car()
bike = Bicycle()
boat = Boat()
start_vehicle(car)
start_vehicle(bike)
start_vehicle(boat)
