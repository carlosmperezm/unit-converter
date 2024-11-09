from typing import Type


class UnitRegistry:

    _unit_registry: dict[str, Type] = {}

    @classmethod
    def register(cls, unit: str, unit_class: Type) -> None:

        if not isinstance(unit_class, type):
            raise ValueError(
                "The provided argument must be a Python class, not an instance."
            )

        if unit in cls._unit_registry:
            raise ValueError(f"Unit {unit} is already registered.")

        cls._unit_registry[unit] = unit_class

    @classmethod
    def get_unit_classes(cls, unit: str) -> dict[str, Type]:
        return cls._unit_registry
