from django.forms import ModelForm
from lavoratr.models import Toilet
from django import forms
from django.contrib.gis import forms as GeoForms

MALE = 'M'
FEMALE = 'F'
UNISEX = 'U'
SEX_CHOICES = (
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    (UNISEX, 'Unisex'),
)


class ToiletForm(ModelForm):
    point = GeoForms.PointField(widget=forms.HiddenInput())
    rating = forms.IntegerField(min_value=1, max_value=10)
    single_occupancy = forms.BooleanField(required=False)
    accesible = forms.BooleanField(required=False)
    station = forms.BooleanField(required=False)

    class Meta:
        model = Toilet

        exclude = [
            'created', 'times_rated', 'times_authenticated',
            'point',
        ]

        fields = [
            'location', 'building', 'rating', 'gender', 'single_occupancy',
            'accesible', 'station',
        ]
