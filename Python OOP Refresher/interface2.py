from abc import ABC, abstractmethod


class ElectronicDevice(ABC):
    @abstractmethod
    def battery_life(self):
        pass


class Smartphone(ElectronicDevice):
    def battery_life(self):
        return "Smartphone battery life: 10 hours."


class Laptop(ElectronicDevice):
    def battery_life(self):
        return "Laptop battery life: 5 hours."


class Smartwatch(ElectronicDevice):
    def battery_life(self):
        return "Smartwatch battery life: 24 hours."


def display_battery_life(device):
    print(device.battery_life())


laptop = Laptop()
phone = Smartphone()
watch = Smartwatch()
display_battery_life(watch)
display_battery_life(laptop)
display_battery_life(phone)

