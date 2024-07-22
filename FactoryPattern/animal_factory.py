from abc import ABC, abstractmethod
from enum import Enum


class AnimalType(Enum):
    DOG = "Dog",
    CAT = "Cat",
    FISH = "Fish"


class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass


class Dog(Animal):
    def get_info(self):
        return f"I am a Dog & my name is {self.name} and age is {self.age}"


class Cat(Animal):
    def get_info(self):
        return f"I am a Cat & my name is {self.name} and age is {self.age}"


class Fish(Animal):
    def get_info(self):
        return f"I am a Fish & my name is {self.name} and age is {self.age}"


class AnimalFactory:
    def create_animal(self, animal_type, context:dict) -> Animal:
        if animal_type == AnimalType.DOG:
            return Dog(context["name"], context["age"])
        elif animal_type == AnimalType.CAT:
            return Cat(context["name"], context["age"])
        elif animal_type == AnimalType.FISH:
            return Fish(context["name"], context["age"])
        else:
            raise ValueError("Invalid Animal type")


animal_factory = AnimalFactory()
dog = animal_factory.create_animal(AnimalType.DOG, {"name":"Sheru","age": 7})
print(dog.get_info())
fish = animal_factory.create_animal(AnimalType.FISH, {"name":"Koala", "age":2})
print(fish.get_info())
cat = animal_factory.create_animal(AnimalType.CAT, {"name":"Cheek","age": 1})
print(cat.get_info())

