from django.shortcuts import render, get_object_or_404
from django.utils import timezone, simplejson
from django.contrib.gis.geos import Point
from lavoratr.models import Toilet, Review
from lavoratr.serializers import ToiletSerializer
from lavoratr.forms import ToiletForm, ReviewForm
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import redirect


def index(request):
    latest_toilet_list = Toilet.objects.all()
    serializer = ToiletSerializer(latest_toilet_list)
    toilets_json = JSONRenderer().render(serializer.data)
    context = {
        'form': ToiletForm,
        'toilets_json': toilets_json,
        'latest_toilet_list': latest_toilet_list
    }
    return render(request, 'lavoratr/toilet.html', context)


def registration(request):
    return render(request, 'lavoratr/user_registration.html')


def login(request):
    return render(request, 'lavoratr/user_login.html')


def login_submit(request):
    username = request.POST['InputUsername']


def get_geojson(request):
    latest_toilet_list = Toilet.objects.all()
    serializer = ToiletSerializer(latest_toilet_list)
    toilets_json = JSONRenderer().render(serializer.data)
    return HttpResponse(toilets_json, content_type="application/json")


def detail(request, toilet_id):
    toilet = get_object_or_404(Toilet, id=toilet_id)
    reviews = Review.objects.filter(toilet=toilet)
    return render(
        request,
        'lavoratr/detail.html',
        {'toilet': toilet, 'reviews': reviews}
    )


def modal_data(request, toilet_id):
    toilet = get_object_or_404(Toilet, id=toilet_id)
    serializer = ToiletSerializer(toilet)
    toilet_json = JSONRenderer().render(serializer.data)
    return HttpResponse(toilet_json, content_type="application/json")


def get_user(username):
    try:
        return User.objects.get(username=username)
    except User.DoesNotExist:
        return None


def registration_submit(request):
    if request.method == "POST":
        email = request.POST['InputEmail']
        username = request.POST['InputUsername']
        password = request.POST['InputPassword']
        password_two = request.POST['InputPasswordConfirm']
        user = get_user(username)
        if password == password_two:
            if user is None:
                user = User.objects.create_user(username, email, password)
                user.save()
                user = authenticate(username=user, password=password)
                return redirect('/')
            else:
                print "User already exists"
                to_json = {"failed": "failed"}
                json = simplejson.dumps(to_json)
                return HttpResponse(json, mimetype='application/json')
        else:
            print "User already exists"
            to_json = {"failed": "failed"}
            json = simplejson.dumps(to_json)
            return HttpResponse(json, mimetype='application/json')


def add_review(request, toilet_id):
    toilet = get_object_or_404(Toilet, id=toilet_id)
    return render(
        request, 'lavoratr/add_review.html',
        {'form': ReviewForm, 'toilet': toilet}
    )


def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            toilet = Toilet.objects.get(id=request.POST['toilet_id'])
            current_time = timezone.now()
            rating = int(request.POST['rating'])
            comment_box = request.POST['comment_box']
            if rating == 1:
                toilet.positive_ratings += 1
            elif rating == 2:
                toilet.negative_ratings += 1
            toilet.save()
            new_review = Review.objects.create(
                toilet=toilet,
                rating=rating,
                comment_box=comment_box,
                created=current_time
            )
            new_review.save()

            return HttpResponse('Yes')

    toilet = get_object_or_404(Toilet, id=request.POST['toilet_id'])
    return render(
        request, 'lavoratr/add_review.html',
        {'form': ReviewForm, 'toilet': toilet}
    )


def add_toilet(request, lat, lng):
    float_lat = float(lat)
    float_lng = float(lng)
    point = Point(float_lng, float_lat)
    return render(
        request, 'lavoratr/add_toilet.html',
        {'form': ToiletForm, 'point': point.hex}
    )


def submit_toilet(request):
    if request.method == 'POST':
        form = ToiletForm(request.POST)
        if form.is_valid():
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

            rating = int(request.POST['rating'])
            if rating == 1:
                pos_rating = 1
                neg_rating = 0
            elif rating == 2:
                pos_rating = 0
                neg_rating = 1

            current_time = timezone.now()
            new_toilet = Toilet.objects.create(
                location=request.POST['location'],
                building=request.POST['building'],
                positive_ratings=pos_rating,
                negative_ratings=neg_rating,
                gender=request.POST['gender'],
                created=current_time,
                single_occupancy=single_occupancy_bool,
                accesible=accesible_bool,
                station=station_bool,
                times_authenticated=1,
                point=Point(
                    float(request.POST['lng']),
                    float(request.POST['lat'])
                )
            )

            new_toilet.save()

            new_id = new_toilet.id
            new_toilet = Toilet.objects.get(id=new_id)

            new_review = Review.objects.create(
                toilet=new_toilet,
                rating=rating,
                comment_box=request.POST['comment_box'],
                created=current_time,
            )
            new_review.save()

            return HttpResponseRedirect('/')
    point = Point(float(request.POST['lng']), float(request.POST['lat']))
    context = {'form': ToiletForm, 'point': point.hex}

    return render(request, 'lavoratr/add_toilet.html', context)
