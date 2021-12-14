from django.shortcuts import render
from .models import City, Hotel


# Create your views here.
def index(request):
    list_cities = City.objects.all()

    context = {"list_cities": list_cities}
    return render(request, 'hotelManager/index.html', context)


def city_details(request, name):
    list_hotels = Hotel.objects.filter(city__name=name)
    nb_hotels = len(list_hotels)
    context = {"list_hotels": list_hotels, "name": name, "nb_hotels": nb_hotels}

    return render(request, 'hotelManager/city_details.html', context)
