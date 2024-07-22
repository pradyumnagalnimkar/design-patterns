from abc import ABC, abstractmethod


class Stock(ABC):
    @abstractmethod
    def attach(self, subscriber):
        pass

    @abstractmethod
    def detach(self, subscriber):
        pass

    @abstractmethod
    def notify_subscribers(self, stock_symbol, price, change_in_price):
        pass

    @abstractmethod
    def set_price(self, stock_symbol,price, change_in_price):
        pass


class Observer(ABC):
    @abstractmethod
    def update(self, stock_symbol, price, change_in_price):
        pass


class PriceDisplay(Observer):
    def update(self, stock_symbol, price, change_in_price):
        print(f"Stock {stock_symbol} is currently priced at {price}")


class ChangeDisplay(Observer):
    def update(self, stock_symbol, price, change_in_price):
        print(f"Change in {stock_symbol} price : {change_in_price}")


class StockData(Stock):
    def __init__(self):
        self._stock_symbol = "ONGC"
        self._price = 400
        self._change_in_price = 3
        self._subscribers = []

    def attach(self, subscriber):
        self._subscribers.append(subscriber)

    def detach(self, subscriber):
        self._subscribers.remove(subscriber)

    def set_price(self, stock_symbol,price, change_in_price=200):
        self._stock_symbol = stock_symbol
        self._price = price
        self._change_in_price = self._price - change_in_price
        self.notify_subscribers(self._stock_symbol, self._price, self._change_in_price)

    def notify_subscribers(self, stock_symbol, price, change_in_price):
        for subscriber in self._subscribers:
            subscriber.update(stock_symbol, price, change_in_price)


if __name__ == "__main__":
    stockdata = StockData()

    price = PriceDisplay()
    change = ChangeDisplay()
    stockdata.attach(price)
    stockdata.attach(change)

    print("Infy Updates:")
    stockdata.set_price("INFY", 1500)
    print("SBI Updates:")
    stockdata.set_price("SBI", 850)







