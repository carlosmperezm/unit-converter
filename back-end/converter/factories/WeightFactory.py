from typing import Type
from converter.models.WeightModels import (
    IWeight,
    Miligram,
    Kilogram,
    Gram,
    Pound,
    Ounce,
)

from converter.UnitRegistry import UnitRegistry


class UnitFactory:

    def __init__(self, number: float, unit_classes: dict[str, Type]):
        if number < 0:
            raise ValueError("The number must be positive")
        self.number = number
        self.unit_classes = unit_classes

    def build(self, unit: str) -> object:
        unit_class = self.unit_classes.get(unit.lower())

        if not unit_class:
            raise ValueError(f"Unit {unit} not found in registry.")

        return unit_class(self.number)
