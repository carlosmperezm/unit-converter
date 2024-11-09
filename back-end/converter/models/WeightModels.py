from abc import ABC, abstractmethod


class IWeight(ABC):

    @abstractmethod
    def pound(self): ...

    @abstractmethod
    def ounce(self): ...

    @abstractmethod
    def gram(self): ...

    @abstractmethod
    def kilogram(self): ...

    @abstractmethod
    def miligram(self): ...


class Pound(IWeight):
    number: float

    def __init__(self, number):
        self.number = float(number)

    def pound(self):
        return self.number

    def ounce(self):
        return self.number * 16

    def gram(self):
        return self.number * 453.6

    def kilogram(self):
        return self.number / 2.205

    def miligram(self):
        return self.number * 453600

    def __str__(self):
        return str(self.number)


class Ounce(IWeight):
    number: float

    def __init__(self, number):
        self.number = float(number)

    def pound(self):
        return self.number / 16

    def ounce(self):
        return self.number

    def gram(self):
        return self.number * 28.35

    def kilogram(self):
        return self.number / 35.274

    def miligram(self):
        return self.number * 28350

    def __str__(self):
        return str(self.number)


class Gram(IWeight):
    number: float

    def __init__(self, number):
        self.number = float(number)

    def pound(self):
        return self.number / 453.6

    def ounce(self):
        return self.number / 28.35

    def gram(self):
        return self.number

    def kilogram(self):
        return self.number / 1000

    def miligram(self):
        return self.number * 1000

    def __str__(self):
        return str(self.number)


class Kilogram(IWeight):
    number: float

    def __init__(self, number):
        self.number = float(number)

    def pound(self):
        return self.number * 2.205

    def ounce(self):
        return self.number * 35.274

    def gram(self):
        return self.number * 1000

    def kilogram(self):
        return self.number

    def miligram(self):
        return self.number * 1000 * 1000

    def __str__(self):
        return str(self.number)


class Miligram(IWeight):
    number: float

    def __init__(self, number):
        self.number = float(number)

    def pound(self):
        return self.number / 453600

    def ounce(self):
        return self.number / 28350

    def gram(self):
        return self.number / 1000

    def kilogram(self):
        return self.number / 1000 / 1000

    def miligram(self):
        return self.number

    def __str__(self):
        return str(self.number)
