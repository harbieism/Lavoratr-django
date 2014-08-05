from django.contrib.gis.db import models
from django.core.exceptions import ValidationError


def validate_rating(value):
    if value < 1 or value > 10:
        raise ValidationError('%s is not a valid rating!' % value)

MALE = 'M'
FEMALE = 'F'
UNISEX = 'U'
SEX_CHOICES = (
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    (UNISEX, 'Unisex'),
)


class Toilet(models.Model):
    location = models.CharField(max_length=50)
    building = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[validate_rating])
    gender = models.CharField(max_length=1,
                              choices=SEX_CHOICES,
                              default=MALE)
    created = models.DateTimeField()
    single_occupancy = models.BooleanField()
    accesible = models.BooleanField()
    station = models.BooleanField()
    lon = models.FloatField()
    lat = models.FloatField()
    times_rated = models.FloatField(default=0)
    times_authenticated = models.FloatField(default=0)

    point = models.PointField()
    objects = models.GeoManager()

    def __unicode__(self):
        return (str(self.location) + ', ' + str(self.building))


class Review(models.Model):
    toilet = models.ForeignKey(Toilet)
    rating = models.IntegerField(validators=[validate_rating])
    comment_box = models.CharField(max_length=127, blank=True)

