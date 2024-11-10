from django.shortcuts import render
from django.http import HttpRequest

from converter.models.Lengthmodels import (
    ILengthMeasure,
    Foot,
    Mile,
    Inch,
    Meter,
    Kilometer,
    Centimeter,
)
from converter.models.WeightModels import (
    IWeight,
    Gram,
    Ounce,
    Miligram,
    Kilogram,
    Pound,
)
from converter.models.TemperatureModels import ITemperature, Celsius, Fahrenheit, Kelvin

from converter.factories.WeightFactory import UnitFactory
from converter.UnitRegistry import UnitRegistry
from converter.units import WeightUnit, LenghtUnit, TemperatureUnit


def length_page(request):
    if request.method == "POST":
        return lenght_converter(request)

    return render(request, "length-page.html")


def weight_page(request: HttpRequest):
    if request.method == "POST":
        return weigth_converter(request)

    return render(request, "weight-page.html")


def temperature_page(request: HttpRequest):
    if request.method == "POST":
        return temperature_converter(request)

    return render(request, "temperature-page.html")


def temperature_converter(request: HttpRequest):
    convert_from: str = request.POST.get("convert_from").lower()
    convert_to: str = request.POST.get("convert_to").lower()
    param_number = float(request.POST.get("number"))
    number_result: float = 0

    unit_classes: dict = UnitRegistry.get_unit_classes(convert_from)

    number: ITemperature = UnitFactory(param_number, unit_classes).build(convert_from)

    conversion_map: dict[str, float] = {
        TemperatureUnit.CELSIUS.value: number.celsius,
        TemperatureUnit.FAHRENHEIT.value: number.fahrenheit,
        TemperatureUnit.KELVIN.value: number.kelvin,
    }

    number_result = conversion_map.get(convert_to)
    if not number_result:
        raise ValueError(f"Uknown unit: {convert_to}")

    context = {
        "convert_from": convert_from,
        "convert_to": convert_to,
        "unit": number,
        "number_result": number_result,
    }

    return render(request, "results.html", context)


def weigth_converter(request):
    convert_from: str = request.POST.get("convert_from").lower()
    convert_to: str = request.POST.get("convert_to").lower()
    param_number = float(request.POST.get("number"))
    number_result: float = 0

    unit_classes: dict = UnitRegistry.get_unit_classes(convert_from)

    number: IWeight = UnitFactory(param_number, unit_classes).build(convert_from)

    conversion_map: dict[str, float] = {
        WeightUnit.GRAM.value: number.gram,
        WeightUnit.KILOGRAM.value: number.kilogram,
        WeightUnit.MILIGRAM.value: number.miligram,
        WeightUnit.OUNCE.value: number.ounce,
        WeightUnit.POUND.value: number.pound,
    }

    number_result = conversion_map.get(convert_to)
    if not number_result:
        raise ValueError(f"Uknown unit: {convert_to}")

    context = {
        "convert_from": convert_from,
        "convert_to": convert_to,
        "unit": number,
        "number_result": number_result,
    }

    return render(request, "results.html", context)


def lenght_converter(request):
    convert_from: str = request.POST.get("convert_from").lower()
    convert_to: str = request.POST.get("convert_to").lower()
    param_number = float(request.POST.get("number"))
    number_result: float = 0

    unit_classes: dict = UnitRegistry.get_unit_classes(convert_from)

    number: ILengthMeasure = UnitFactory(param_number, unit_classes).build(convert_from)

    conversion_map: dict[str, float] = {
        LenghtUnit.FOOT.value: number.foot,
        LenghtUnit.INCH.value: number.inch,
        LenghtUnit.MILE.value: number.mile,
        LenghtUnit.METER.value: number.meter,
        LenghtUnit.KILOMETER.value: number.kilometer,
        LenghtUnit.CENTIMETER.value: number.centimeter,
    }

    number_result = conversion_map.get(convert_to)
    if not number_result:
        raise ValueError(f"Uknown unit: {convert_to}")

    context = {
        "convert_from": convert_from,
        "convert_to": convert_to,
        "unit": number,
        "number_result": number_result,
    }

    return render(request, "results.html", context)
