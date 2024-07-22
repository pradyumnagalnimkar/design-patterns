from abc import ABC, abstractmethod
from enum import Enum, auto


class VehicleType(Enum):
    CAR = "Car"
    MOTORCYCLE = "Motorcycle"
    BICYCLE = "Bicycle"


class Vehicle(ABC):
    @abstractmethod
    def get_name(self):
        pass


class Car(Vehicle):
    def get_name(self):
        return "Car"


class Bicycle(Vehicle):
    def get_name(self):
        return "Bicycle"


class Motorcycle(Vehicle):
    def get_name(self):
        return "Motorcycle"


class VehicleFactory:
    def create_vehicle(self, vehicle):
        if vehicle == VehicleType.CAR:
            return Car()
        elif vehicle == VehicleType.BICYCLE:
            return Bicycle()
        elif vehicle == VehicleType.MOTORCYCLE:
            return Motorcycle()
        else:
            raise ValueError("Invalid vehicle type")


vehicle_factory = VehicleFactory()
car = vehicle_factory.create_vehicle(VehicleType.MOTORCYCLE)
print(car.get_name())
bicycle = vehicle_factory.create_vehicle(VehicleType.CAR)
print(bicycle.get_name())
motorcycle = vehicle_factory.create_vehicle(VehicleType.BICYCLE)
print(motorcycle.get_name())
