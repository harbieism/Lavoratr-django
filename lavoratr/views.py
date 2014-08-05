from django.shortcuts import render, get_object_or_404
from lavoratr.models import Toilet
from lavoratr.serializers import ToiletSerializer
from rest_framework.renderers import JSONRenderer


def index(request):
    latest_toilet_list = Toilet.objects.all()
    serializer = ToiletSerializer(latest_toilet_list)
    toilets_json = JSONRenderer().render(serializer.data)
    context = {
        'toilets_json': toilets_json,
        'latest_toilet_list': latest_toilet_list
    }
    return render(request, 'lavoratr/toilet.html', context)


def detail(request, toilet_id):
    toilet = get_object_or_404(Toilet, id=toilet_id)
    return render(request, 'lavoratr/detail.html', {'toilet': toilet})


def add_toilet(request, lat, lng):
    newLatLng = [lat, lng]
    return render(request, 'lavoratr/add_toilet.html', {'newLatLng': newLatLng})
