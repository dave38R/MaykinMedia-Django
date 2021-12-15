from django import forms
from .models import City, Hotel


class CreateHotel(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ("id_hotel", "name")


class CreateCity(forms.ModelForm):
    class Meta:
        model = City
        fields = ("name", "code_name")


# class UploadFileForm(forms.Form):
#     file = forms.ImageField()
