from django.shortcuts import render


def length_page(request):
    return render(request, "length-page.html")


def weight_page(request):
    return render(request, "weight-page.html")


def temperature_page(request):
    return render(request, "temperature-page.html")
