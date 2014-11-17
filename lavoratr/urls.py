from django.conf.urls import patterns, url
from lavoratr import views
from djgeojson.views import GeoJSONLayerView
from lavoratr.models import Toilet

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(
        r'^add_review/(?P<toilet_id>\d+)/$',
        views.add_review,
        name='add_review'
    ),
    url(r'^detail/(?P<toilet_id>\d+)/$', views.detail, name='detail'),
    url(
        r'^data.geojson$',
        GeoJSONLayerView.as_view(model=Toilet),
        name='data'
    ),
    url(
        r'^add_toilet/(?P<lat>-?\d+\.\d+)/(?P<lng>-?\d+\.\d+)/$',
        views.add_toilet,
        name='add_toilet'
    ),
    url(r'^submit_toilet/$', views.submit_toilet, name='submit_toilet'),
    url(r'^get_modal_data/(?P<toilet_id>\d+)/$', views.modal_data, name='modal_data'),
    url(r'^submit_review/$', views.submit_review, name='submit_review'),
    url(r'^get.geojson.js$', views.get_geojson, name='get_geojson'),
)
