from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('city/<str:name>/', views.city_details, name='city_details'),
    path('add_hotel_in_<str:name>/', views.add_hotel, name="add_hotel"),
    path('add_city/', views.add_city, name="add_city"),

]




