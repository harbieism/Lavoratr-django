from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^lavoratr/', include('lavoratr.urls', namespace="lavoratr")),
    url(r'^admin/', include(admin.site.urls)),
)
