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

from converter.factories.WeightFactory import UnitFactory
from converter.UnitRegistry import UnitRegistry
from converter.units import WeightUnit, LenghtUnit


def length_page(request):
    if request.method == "POST":
        return lenght_converter(request)

    return render(request, "length-page.html")


def weight_page(request: HttpRequest):
    if request.method == "POST":
        return weigth_converter(request)

    return render(request, "weight-page.html")


def temperature_page(request):
    return render(request, "temperature-page.html")


def weigth_converter(request):
    convert_from: str = request.POST.get("convert_from").lower()
    convert_to: str = request.POST.get("convert_to").lower()
    param_number = float(request.POST.get("number"))
    number_result: float = 0

    unit_classes: dict = UnitRegistry.get_unit_classes(convert_from)

    number: IWeight = UnitFactory(param_number, unit_class).build(convert_from)

    if convert_to == WeightUnit.GRAM:
        number_result = number.gram()
    elif convert_to == WeightUnit.KILOGRAM:
        number_result = number.kilogram()
    elif convert_to == WeightUnit.MILIGRAM:
        number_result = number.miligram()
    elif convert_to == WeightUnit.OUNCE:
        number_result = number.ounce()
    elif convert_to == WeightUnit.POUND:
        number_result = number.pound()

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

    if convert_to == "mile":
        number_result = number.mile
    elif convert_to == "foot":
        number_result = number.foot
    elif convert_to == "meter":
        number_result = number.meter
    elif convert_to == "kilometer":
        number_result = number.kilometer
    elif convert_to == "centimeter":
        number_result = number.centimeter
    elif convert_to == "inch":
        number_result = number.inch

    context = {
        "convert_from": convert_from,
        "convert_to": convert_to,
        "unit": number,
        "number_result": number_result,
    }

    return render(request, "results.html", context)
