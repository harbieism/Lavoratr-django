from django.contrib import admin
from lavoratr.models import Toilet


class ToiletAdmin(admin.ModelAdmin):
    fields = [
        'building', 'location', 'positive_ratings', 'negative_ratings',
        'gender', 'single_occupancy', 'accesible',
        'station', 'created', 'comment_box',
        'lon', 'lat', 'point'
    ]

    list_display = (
        'building', 'location', 'positive_ratings', 'negative_ratings',
        'created'
    )
admin.site.register(Toilet, ToiletAdmin)
