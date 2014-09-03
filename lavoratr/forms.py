from django import forms
from django.contrib.gis import forms as GeoForms
from django.core.exceptions import ValidationError

MALE = 'M'
FEMALE = 'F'
UNISEX = 'U'
SEX_CHOICES = (
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    (UNISEX, 'Unisex'),
)


def validate_length(value):
    if len(value) < 5:
        raise ValidationError('%s is not longer than 5 characters' % value)


'''NOTE:  for rating: 1=like, 2 = dislike, 3 = neutral'''


class ToiletForm(forms.Form):
    point = GeoForms.PointField(widget=forms.HiddenInput())
    location = forms.CharField(
        max_length=50, validators=[validate_length], required=True
    )
    building = forms.CharField(
        max_length=50, validators=[validate_length], required=True
    )
    gender = forms.ChoiceField(choices=SEX_CHOICES)
    rating = forms.IntegerField(min_value=1, max_value=3)
    single_occupancy = forms.BooleanField(required=False)
    accesible = forms.BooleanField(required=False)
    station = forms.BooleanField(required=False)
    comment_box = forms.CharField(max_length=127, required=False)


class ReviewForm(forms.Form):
    rating = forms.IntegerField(min_value=1, max_value=3)
    comment_box = forms.CharField(max_length=127, required=False)
