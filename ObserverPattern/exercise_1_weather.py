from abc import ABC, abstractmethod


class WeatherData(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def set_measurements(self, temperature, humidity, pressure):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class Observer(ABC):
    @abstractmethod
    def update(self, temperature, humidity, pressure):
        pass


class CurrentConditionDisplay(Observer):
    def update(self, temperature, humidity, pressure):
        print(f"Current Conditions: Temperature: {temperature}, Humidity: {humidity}, Pressure: {pressure}")


class StatisticsDisplay(Observer):
    def update(self, temperature, humidity, pressure):
        print(f"Statistics Conditions: Temperature: {temperature+5}, Humidity: {humidity+5}, Pressure: {pressure-5}")


class ForecastDisplay(Observer):
    def update(self, temperature, humidity, pressure):
        print(f"Forecast Conditions: Temperature: {temperature+10}, Humidity: {humidity+10}, Pressure: {pressure-10}")


class Weather(WeatherData):
    def __init__(self):
        self._observers = []
        self._temperature = 32
        self._humidity = 28
        self._pressure = 37

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def set_measurements(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify_observers()

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)


if __name__ == "__main__":
    weather = Weather()

    current = CurrentConditionDisplay()
    stats = StatisticsDisplay()
    forecast = ForecastDisplay()

    weather.attach(current)
    weather.attach(stats)
    weather.attach(forecast)

    print("On Day 1")
    weather.set_measurements(100, 100, 100)

    print("On Day 2")
    weather.set_measurements(50, 50, 50)

    weather.detach(current)
    weather.detach(forecast)
    print("On Day 3")
    weather.set_measurements(30, 30, 30)





