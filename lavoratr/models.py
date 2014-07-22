from django.contrib.gis.db import models
from django.core.exceptions import ValidationError


def validate_rating(value):
    if value < 1 or value > 10:
        raise ValidationError(u'%s is not a valid rating!' % value)


class Toilet(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    UNISEX = 'U'
    SEX_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (UNISEX, 'Unisex'),
    )
    location = models.CharField(max_length=50)
    building = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[validate_rating])
    gender = models.CharField(max_length=1,
                              choices=SEX_CHOICES,
                              default=MALE)
    single_occupancy = models.BooleanField()
    accesible = models.BooleanField()
    station = models.BooleanField()
    comment_box = models.CharField(max_length=127, blank=True)
    lon = models.FloatField()
    lat = models.FloatField()

    point = models.PointField()
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name
