from django.shortcuts import render
from converter.models import (
    ILengthMeasure,
    Foot,
    Mile,
    Inch,
    Meter,
    Kilometer,
    Centimeter,
)


def length_page(request):
    print("wiii", request.POST)
    if request.method == "POST":
        return lenght_converter(request)

    return render(request, "length-page.html")


def weight_page(request):
    return render(request, "weight-page.html")


def temperature_page(request):
    return render(request, "temperature-page.html")


def lenght_converter(request):
    convert_from: str = request.POST.get("convert_from")
    convert_to: str = request.POST.get("convert_to")
    param_number = request.POST.get("number")
    number: ILengthMeasure
    number_result: float = 0

    if convert_from.lower() == "mile":
        number = Mile(param_number)
    elif convert_from.lower() == "foot":
        number = Foot(param_number)
    elif convert_from.lower() == "meter":
        number = Meter(param_number)
    elif convert_from.lower() == "kilometer":
        number = Kilometer(param_number)
    elif convert_from.lower() == "centimeter":
        number = Centimeter(param_number)
    elif convert_from.lower() == "inch":
        number = Inch(param_number)

    if convert_to.lower() == "mile":
        number_result = number.mile
    elif convert_to.lower() == "foot":
        number_result = number.foot
    elif convert_to.lower() == "meter":
        number_result = number.meter
    elif convert_to.lower() == "kilometer":
        number_result = number.kilometer
    elif convert_to.lower() == "centimeter":
        number_result = number.centimeter
    elif convert_to.lower() == "inch":
        number_result = number.inch

    context = {
        "convert_from": convert_from,
        "convert_to": convert_to,
        "unit": number,
        "number_result": number_result,
    }

    return render(request, "results.html", context)
