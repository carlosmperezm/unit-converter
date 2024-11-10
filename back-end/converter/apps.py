from django.apps import AppConfig

from converter.UnitRegistry import UnitRegistry

from converter.units import WeightUnit, LenghtUnit, TemperatureUnit

from converter.models.Lengthmodels import Inch, Foot, Mile, Meter, Kilometer, Centimeter
from converter.models.WeightModels import Ounce, Gram, Pound, Kilogram, Miligram
from converter.models.TemperatureModels import Celsius, Fahrenheit, Kelvin


class ConverterConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "converter"

    def ready(self):
        # Lenght units registry
        UnitRegistry.register(LenghtUnit.INCH.value, Inch)
        UnitRegistry.register(LenghtUnit.FOOT.value, Foot)
        UnitRegistry.register(LenghtUnit.MILE.value, Mile)
        UnitRegistry.register(LenghtUnit.METER.value, Meter)
        UnitRegistry.register(LenghtUnit.KILOMETER.value, Kilometer)
        UnitRegistry.register(LenghtUnit.CENTIMETER.value, Centimeter)

        # Weight units registry
        UnitRegistry.register(WeightUnit.OUNCE.value, Ounce)
        UnitRegistry.register(WeightUnit.GRAM.value, Gram)
        UnitRegistry.register(WeightUnit.POUND.value, Pound)
        UnitRegistry.register(WeightUnit.KILOGRAM.value, Kilogram)
        UnitRegistry.register(WeightUnit.MILIGRAM.value, Miligram)

        # Temperature units registery
        UnitRegistry.register(TemperatureUnit.CELSIUS.value, Celsius)
        UnitRegistry.register(TemperatureUnit.FAHRENHEIT.value, Fahrenheit)
        UnitRegistry.register(TemperatureUnit.KELVIN.value, Kelvin)
