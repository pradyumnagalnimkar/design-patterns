from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, total):
        pass


class NoDiscount(DiscountStrategy):
    def apply_discount(self, total):
        return total


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, total):
        return total - ((total * self.percentage)/100)


class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, fixed_amount):
        self.fixed_amount = fixed_amount

    def apply_discount(self, total):
        return total - self.fixed_amount


class ShoppingCart:
    def __init__(self, discount_strategy: DiscountStrategy):
        self.discount_strategy = discount_strategy
        self.items = {}

    def add_item(self, item:str, price: float):
        self.items[item] = price

    def remove_item(self, item:str):
        del self.items[item]

    def get_total(self):
        total = 0
        for item_value in self.items.values():
            total += item_value
        return total

    def get_total_after_discount(self):
        total = self.get_total()
        return self.discount_strategy.apply_discount(total)


discount_strategy = PercentageDiscount(5)
cart = ShoppingCart(discount_strategy)
cart.add_item('Item 1', 45)
cart.add_item('Item 2', 45)
cart.add_item('Item 3', 10)
print(f"Total Cart Value: {cart.get_total()}")
print(f"Total Cart Value after discount: {cart.get_total_after_discount()}")



