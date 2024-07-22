from abc import ABC, abstractmethod


class Computer:
    def __init__(self):
        self.processor = ''
        self.memory = ''
        self.storage = ''
        self.graphics_card = ''
        self.operating_system = ''
        self.extras = []


class ComputerBuilder(ABC):
    @abstractmethod
    def add_processor(self):
        pass

    @abstractmethod
    def add_memory(self):
        pass

    @abstractmethod
    def add_storage(self):
        pass

    @abstractmethod
    def add_graphics_card(self):
        pass

    @abstractmethod
    def add_operating_system(self):
        pass

    @abstractmethod
    def add_extras(self):
        pass


class CustomComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def add_processor(self, processor):
        self.computer.processor = processor

    def add_memory(self, memory):
        self.computer.memory = memory

    def add_storage(self, storage):
        self.computer.storage = storage

    def add_graphics_card(self, graphics_card):
        self.computer.graphics_card = graphics_card

    def add_operating_system(self, operating_system):
        self.computer.operating_system = operating_system

    def add_extras(self, extras):
        self.computer.extras = extras


class ComputerDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_computer(self, specs):
        self.builder.add_processor(specs["processor"])
        self.builder.add_memory(specs["memory"])
        self.builder.add_storage(specs["storage"])
        self.builder.add_graphics_card(specs["graphics_card"])
        self.builder.add_operating_system(specs["operating_system"])
        self.builder.add_extras(specs["extras"])


test_specs = {
    'processor': 'Intel Core i5',
    'memory': '8GB',
    'storage': '512GB SSD',
    'graphics_card': 'Integrated',
    'operating_system': 'Windows 11',
    'extras': ['Wi-Fi']
}

expected_specs = {
    'processor': 'Intel Core i5',
    'memory': '8GB',
    'storage': '512GB SSD',
    'graphics_card': 'Integrated',
    'operating_system': 'Windows 11',
    'extras': ['Wi-Fi']
}

builder = CustomComputerBuilder()
director = ComputerDirector(builder)
director.build_computer(test_specs)
computer = builder.computer

assert computer.__dict__ == expected_specs
