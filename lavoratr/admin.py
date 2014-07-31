from django.contrib import admin
from lavoratr.models import Toilet


class ToiletAdmin(admin.ModelAdmin):
    fields = [
        'building', 'location', 'rating',
        'gender', 'single_occupancy', 'accesible',
        'station', 'created', 'comment_box',
        'lon', 'lat', 'point'
    ]

    list_display = ('building', 'location', 'rating', 'created')
admin.site.register(Toilet, ToiletAdmin)
