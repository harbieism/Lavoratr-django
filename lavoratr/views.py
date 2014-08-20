from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib.gis.geos import Point, GEOSGeometry
from lavoratr.models import Toilet, Review
from lavoratr.serializers import ToiletSerializer
from lavoratr.forms import ToiletForm, ReviewForm
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


def add_review(request, toilet_id):
    toilet = get_object_or_404(Toilet, id=toilet_id)
    return render(
        request, 'lavoratr/add_review.html',
        {'form': ReviewForm, 'toilet': toilet}
    )


def submit_review(request):
    toilet = Toilet.objects.get(id=request.POST['id'])
    current_time = timezone.now()
    rating = int(request.POST['rating'])
    comment_box = request.POST['comment_box']
    toilet.rating += rating
    toilet.times_rated += 1
    toilet.save()
    new_review = Review.objects.create(
        toilet=toilet,
        rating=rating,
        comment_box=comment_box,
        created=current_time
    )
    new_review.save()

    return render(request, 'lavoratr/detail.html', {'toilet': toilet})


def add_toilet(request, lat, lng):
    float_lat = float(lat)
    float_lng = float(lng)
    point = Point(float_lng, float_lat)
    return render(
        request, 'lavoratr/add_toilet.html',
        {'form': ToiletForm, 'point': point.hex}
    )


def submit_toilet(request):
    if 'single_occupancy' in request.POST:
        single_occupancy_bool = True
    else:
        single_occupancy_bool = False

    if 'accesible' in request.POST:
        accesible_bool = True
    else:
        accesible_bool = False

    if 'station' in request.POST:
        station_bool = True
    else:
        station_bool = False

    current_time = timezone.now()
    new_toilet = Toilet.objects.create(
        location=request.POST['location'],
        building=request.POST['building'],
        rating=request.POST['rating'],
        gender=request.POST['gender'],
        created=current_time,
        single_occupancy=single_occupancy_bool,
        accesible=accesible_bool,
        station=station_bool,
        times_rated=1,
        times_authenticated=1,
        point=GEOSGeometry(request.POST['point'])
    )
    new_toilet.save()

    new_id = new_toilet.id
    new_toilet = Toilet.objects.get(id=new_id)

    new_review = Review.objects.create(
        toilet=new_toilet,
        rating=request.POST['rating'],
        comment_box=request.POST['comment_box'],
        created=current_time,
    )
    new_review.save()

    return render(request, 'lavoratr/detail.html', {'toilet': new_toilet})
