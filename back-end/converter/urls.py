from django.urls import path

from converter.views import length_page, weight_page, temperature_page

urlpatterns = [
    path("length/", length_page, name="length"),
    path("weight/", weight_page, name="weight"),
    path("temperature/", temperature_page, name="temperature"),
]
