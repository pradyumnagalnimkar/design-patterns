from abc import ABC, abstractmethod


class Shipping(ABC):
    @abstractmethod
    def calculate_shipping_cost(self, weight, ):
        pass


class FedexShipping(Shipping):
    def calculate_shipping_cost(self, weight):
        return weight * 2.5


class UPSShipping(Shipping):
    def calculate_shipping_cost(self, weight):
        return weight * 3
    

class DHLShipping(Shipping):
    def calculate_shipping_cost(self, weight):
        return weight * 4


class ShippingCost:
    def __init__(self, shipper):
        self.shipper = shipper

    def get_shipping_cost(self, weight):
        return self.shipper.calculate_shipping_cost(weight)


shipping = ShippingCost(FedexShipping())
print(shipping.get_shipping_cost(100))
shipping = ShippingCost(DHLShipping())
print(shipping.get_shipping_cost(100))
shipping = ShippingCost(UPSShipping())
print(shipping.get_shipping_cost(100))
