from django import forms
from .models import Cities, CityCars


class CityForm(forms.ModelForm):
    class Meta:
        model = Cities
        fields = "__all__"


class CityUpdateForm(forms.ModelForm):
    class Meta:
        model = Cities
        exclude = ('city_file', )


class CityCarForm(forms.ModelForm):
    class Meta:
        model = CityCars
        fields = '__all__'
        widgets = {'city': forms.HiddenInput()}
        # exclude = ('city', )
