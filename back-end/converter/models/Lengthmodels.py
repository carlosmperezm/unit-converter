from abc import ABC, abstractmethod


class ILengthMeasure(ABC):

    @abstractmethod
    def meter(self): ...

    @abstractmethod
    def kilometer(self): ...

    @abstractmethod
    def centimeter(self): ...

    @abstractmethod
    def mile(self): ...

    @abstractmethod
    def inch(self): ...

    @abstractmethod
    def foot(self): ...


class Inch(ILengthMeasure):
    number: float

    def __init__(self, number: float):
        self.number = float(number)

    @property
    def meter(self):
        return self.number / 39.37

    @property
    def kilometer(self):
        return self.number / 39370

    @property
    def centimeter(self):
        return self.number * 2.54

    @property
    def inch(self):
        return self.number

    @property
    def foot(self):
        return self.number / 12

    @property
    def mile(self):
        return self.number / 63360

    def __str__(self):
        return str(self.number)


class Foot(ILengthMeasure):
    number: float

    def __init__(self, number: float):
        self.number = float(number)

    @property
    def meter(self):
        return self.number * 0.3048

    @property
    def kilometer(self):
        return self.number * 0.0003048

    @property
    def centimeter(self):
        return self.number * 30.48

    @property
    def mile(self):
        return self.number * 0.000189394

    @property
    def inch(self):
        return self.number * 12

    @property
    def foot(self):
        return self.number

    def __str__(self):
        return str(self.number)


class Mile(ILengthMeasure):
    number: float

    def __init__(self, number: float):
        self.number = float(number)

    @property
    def meter(self):
        return self.number * 1609.34

    @property
    def kilometer(self):
        return self.number * 1.60934

    @property
    def centimeter(self):
        return self.number * 160934

    @property
    def foot(self):
        return self.number * 5280

    @property
    def inch(self):
        return self.number * 63360

    @property
    def mile(self):
        return self.number

    def __str__(self):
        return str(self.number)


class Meter(ILengthMeasure):
    number: float

    def __init__(self, number: float):
        self.number = float(number)

    @property
    def meter(self):
        return self.number

    @property
    def kilometer(self):
        return self.number / 1000

    @property
    def centimeter(self):
        return self.number * 100

    @property
    def foot(self):
        return self.number * 3.281

    @property
    def inch(self):
        return self.number * 39.37

    @property
    def mile(self):
        return self.number / 1609

    def __str__(self):
        return str(self.number)


class Kilometer(ILengthMeasure):
    number: float

    def __init__(self, number: float):
        self.number = float(number)

    @property
    def meter(self):
        return self.number * 1000

    @property
    def kilometer(self):
        return self.number

    @property
    def centimeter(self):
        return self.number * 100000

    @property
    def foot(self):
        return self.number * 3281

    @property
    def inch(self):
        return self.number * 39370

    @property
    def mile(self):
        return self.number / 1.609

    def __str__(self):
        return str(self.number)


class Centimeter(ILengthMeasure):
    number: float

    def __init__(self, number: float):
        self.number = float(number)

    @property
    def meter(self):
        return self.number / 100

    @property
    def kilometer(self):
        return self.number / 100000

    @property
    def centimeter(self):
        return self.number * 100000

    @property
    def foot(self):
        return self.number * 3281

    @property
    def inch(self):
        return self.number * 39370

    @property
    def mile(self):
        return self.number / 1.609

    def __str__(self):
        return str(self.number)
