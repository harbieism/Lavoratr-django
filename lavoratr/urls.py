from django.conf.urls import patterns, url
from lavoratr import views
from djgeojson.views import GeoJSONLayerView
from lavoratr.models import Toilet

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<toilet_id>\d+)/$', views.detail, name='detail'),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(
        model=Toilet
    ), name='data'),
)
