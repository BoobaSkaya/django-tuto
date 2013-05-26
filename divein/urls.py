from django.conf.urls import patterns, url

from divein import views

urlpatterns = patterns('',
	url(r'^$'             		 , views.index						 , name='index'),
    url(r'^divers/$'             , views.DiverListView.as_view()     , name='divers'),
    url(r'^diver/(?P<pk>\d+)/$'  , views.DiverDetailView.as_view()   , name='diver'),
    url(r'^profile/$'            , views.profile                     , name='profile'),
    url(r'^dive/(?P<pk>\d+)/$'   , views.dive_detail    			 , name='dive'),
    url(r'^dive/add/$'           , views.dive_form                   , name='dive_add'),
    url(r'^spot/(?P<pk>\d+)/$'   , views.SpotDetailView.as_view()    , name='spot'),
    url(r'^spots$'               , views.SpotListView.as_view()      , name='spots'),
    url(r'^spot/(?P<pk>\d+)/dive_add$'   , views.spot_add_dive       , name='spot_add_dive'),
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'divein/login.html'}, name='login'),
    url(r'^logout$'               , views.logoutv                    , name='logout'),
    # url(r'^dive/(?P<pk>\d+)/$'   , views.DiveDetailView.as_view()    , name='dive'),
)