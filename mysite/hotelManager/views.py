from django.shortcuts import render, redirect
from .models import City, Hotel
from .get_data import cities, hotels, funcity
from .forms import CreateHotel, CreateCity


# Create your views here.
def index(request):
    # Delete the existing data
    for city in City.objects.all():
        city.delete()
    for hotel in Hotel.objects.all():
        hotel.delete()

    # Add the new data
    nb_cities = len(cities[0])
    nb_hotels = len(hotels[0])

    # Here, we add the cities
    for i in range(nb_cities):
        City.objects.create(name=cities[0][i], code_name=cities[1][i])

    Cities = City.objects.all()  # In order to use funcity we need to define this variable

    for i in range(nb_hotels):
        Hotel.objects.create(city=funcity(Cities, hotels[0][i]), id_hotel=hotels[1][i], name=hotels[2][i])

    list_cities = Cities

    context = {"list_cities": list_cities}
    return render(request, 'hotelManager/index.html', context)


def city_details(request, name):
    list_hotels = Hotel.objects.filter(city__name=name)  # It's city__name and not city.name for some reason
    nb_hotels = len(list_hotels)
    context = {"list_hotels": list_hotels, "name": name, "nb_hotels": nb_hotels}
    return render(request, 'hotelManager/city_details.html', context)


def add_city(request):
    if request.method == "POST":
        form = CreateHotel(request.POST)
        if form.is_valid():
            hotel = form.save(commit=False)
            hotel.save()
            return redirect("index")
    else:
        form = CreateCity()
    return render(request, 'hotelManager/index.html', {'form': form})


def add_hotel(request, name):
    if request.method == "POST":
        form = CreateHotel(request.POST)
        if form.is_valid():
            hotel = form.save(commit=False)
            hotel.city = City.objects.filter(name=name)[0]
            hotel.save()
            return redirect("city_details", name=name)

    else:
        form = CreateHotel()
    return render(request, 'hotelManager/add_hotel.html', {'form': form})
