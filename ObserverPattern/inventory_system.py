from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, product_name, new_stock):
        pass


class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self, product_name, new_stock):
        pass


class StoreManager(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, product_name, new_stock):
        print(f"{self.name} was notified that {product_name} stock level is now {new_stock}")


class Inventory(Subject):
    def __init__(self, threshold=10):
        self._observers = []
        self._products = {}
        self._threshold = threshold

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, product_name, new_stock):
        for observer in self._observers:
            observer.update(product_name, new_stock)

    def update_stock(self, product_name, new_stock):
        self._products.update({product_name: new_stock})
        if new_stock < self._threshold:
            self.notify(product_name, new_stock)


if __name__ == "__main__":
    inventory = Inventory()

    inventory._products = {
        'Apples': 10,
        'Bananas': 20,
        'Grapes': 30
    }

    manager1 = StoreManager("Alice")
    manager2 = StoreManager("Bob")

    inventory.attach(manager1)
    inventory.attach(manager2)

    print("Update after Stock level 1")
    inventory.update_stock('Apples', 5) #should notify both managers
    print("Update after Stock level 2")
    inventory.update_stock('Bananas', 7) #should notify both managers
    print("Update after stock level 3")
    inventory.update_stock('Bananas', 15)  # should not notify any manager

    inventory.detach(manager1)
    print("Update after stock level 4")
    inventory.update_stock('Grapes', 4)  # should notify any manager2 only