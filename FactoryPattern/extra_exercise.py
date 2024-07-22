from abc import ABC, abstractmethod
from enum import Enum


class SpaceshipType(Enum):
    MILLENIUMFALCON = "MilleniumFalcon",
    UNSCINFINITY = "UNSCInfinity",
    USSENTERPRISE = "USSEnterprise",
    SERENITY = "Serenity"


class Spaceship(ABC):
    def __init__(self, position, size, displayName, speed):
        self.position = position
        self.size = size
        self.displayName = displayName
        self.speed = speed

    @abstractmethod
    def get_info(self):
        pass


class MilleniumFalcon(Spaceship):
    def get_info(self):
        return f"{self.displayName} of {self.size} is at {self.position} and will travel with a speed of {self.speed}"


class UNSCInfinity(Spaceship):
    def get_info(self):
        return f"{self.displayName} of {self.size} is at {self.position} and will travel with a speed of {self.speed}"


class USSEnterprise(Spaceship):
    def get_info(self):
        return f"{self.displayName} of {self.size} is at {self.position} and will travel with a speed of {self.speed}"


class Serenity(Spaceship):
    def get_info(self):
        return f"{self.displayName} of {self.size} is at {self.position} and will travel with a speed of {self.speed}"


class SpaceshipFactory:
    def create_spaceship(self, space_ship, context: dict):
        if space_ship == SpaceshipType.MILLENIUMFALCON:
            return MilleniumFalcon(context["position"], context["size"], context["displayName"], context["speed"])
        elif space_ship == SpaceshipType.UNSCINFINITY:
            return UNSCInfinity(context["position"], context["size"], context["displayName"], context["speed"])
        elif space_ship == SpaceshipType.USSENTERPRISE:
            return USSEnterprise(context["position"], context["size"], context["displayName"], context["speed"])
        elif space_ship == SpaceshipType.SERENITY:
            return Serenity(context["position"], context["size"], context["displayName"], context["speed"])


spaceship_factory = SpaceshipFactory()
milleniumfalcon = spaceship_factory.create_spaceship(SpaceshipType.MILLENIUMFALCON,
                                                     {"position": "top", "size": "400 Ton", "displayName": "millenia",
                                                      "speed": "250 km/hr"})
print(milleniumfalcon.get_info())
unsc = spaceship_factory.create_spaceship(SpaceshipType.UNSCINFINITY,
                                                     {"position": "right", "size": "300 Ton", "displayName": "unsc",
                                                      "speed": "450 km/hr"})
print(unsc.get_info())
uss = spaceship_factory.create_spaceship(SpaceshipType.USSENTERPRISE,
                                                     {"position": "bottom", "size": "800 Ton", "displayName": "ussc",
                                                      "speed": "150 km/hr"})
print(uss.get_info())
serenity = spaceship_factory.create_spaceship(SpaceshipType.SERENITY,
                                                     {"position": "left", "size": "100 Ton", "displayName": "sere",
                                                      "speed": "1050 km/hr"})
print(serenity.get_info())

