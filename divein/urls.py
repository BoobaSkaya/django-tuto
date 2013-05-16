from django.conf.urls import patterns, url

from divein import views

urlpatterns = patterns('',
    url(r'^$'                       , views.DiverListView.as_view()     , name='divers'),
    url(r'^(?P<pk>\d+)/$'           , views.DiverDetailView.as_view()   , name='diver'),
)