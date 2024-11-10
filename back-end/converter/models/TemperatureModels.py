from abc import ABC, abstractmethod


class ITemperature(ABC):

    @abstractmethod
    def celsius(self): ...

    @abstractmethod
    def fahrenheit(self): ...

    @abstractmethod
    def kelvin(self): ...


class Celsius(ITemperature):
    number: float

    def __init__(self, number: float):
        self.number = float(number)

    def celsius(self):
        return self.number

    def kelvin(self):
        return self.number + 273.15

    def fahrenheit(self):
        return (self.number * 9 / 5) + 32

    def __str__(self):
        return str(self.number)


class Fahrenheit(ITemperature):
    number: float

    def __init__(self, number: float):
        self.number = float(number)

    def celsius(self):
        return (self.number - 32) * 5 / 9

    def kelvin(self):
        return (self.number - 32) * 5 / 9 + 273.15

    def fahrenheit(self):
        return self.number

    def __str__(self):
        return str(self.number)


class Kelvin(ITemperature):
    number: float

    def __init__(self, number: float):
        self.number = float(number)

    def celsius(self):
        return self.number - 273.15

    def kelvin(self):
        return self.number

    def fahrenheit(self):
        return (self.number - 273.15) * 9 / 5 + 32

    def __str__(self):
        return str(self.number)
