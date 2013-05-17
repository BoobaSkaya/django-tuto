from django.conf.urls import patterns, url

from divein import views

urlpatterns = patterns('',
	url(r'^$'             		 , views.index						 , name='index'),
    url(r'^divers/$'             , views.DiverListView.as_view()     , name='divers'),
    url(r'^diver/(?P<pk>\d+)/$'  , views.DiverDetailView.as_view()   , name='diver'),
    url(r'^dive/(?P<pk>\d+)/$'   , views.dive_detail    			 , name='dive'),
    url(r'^spot/(?P<pk>\d+)/$'   , views.SpotDetailView.as_view()    , name='spot'),
    # url(r'^dive/(?P<pk>\d+)/$'   , views.DiveDetailView.as_view()    , name='dive'),
)