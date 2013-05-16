from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from polls.models import Poll
from polls.models import Choice

# admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    #What to display?
    list_display = ('question', 'pub_date', 'was_published_recently')
    #How to display Choices?
    inlines = [ChoiceInline]

    list_filter     = ['pub_date']
    search_fields   = ['question']
    date_hierarchy  = 'pub_date'

admin.site.register(Poll, PollAdmin)

from divein.models import Diver,Level,Federation,Graduate,Club,Spot,Dive,DiveTag,DivePart

class DiverAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal', {'fields': ['first_name', 'last_name', 'email', 'birth_date']}),
        #('Diving'  , {'fields': ['levels']}),
    ]
    #What to display?
    list_display = ('first_name', 'last_name')
    #list_filter    = ['levels']


admin.site.register(Diver, DiverAdmin)
admin.site.register(Graduate)
admin.site.register(Level)
admin.site.register(Club)
admin.site.register(Dive)
admin.site.register(Spot)
admin.site.register(Federation)
admin.site.register(DiveTag)
admin.site.register(DivePart)

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/' , include(admin.site.urls)),
    url(r'^polls/' , include('polls.urls' , namespace='polls')),
    url(r'^divein/', include('divein.urls', namespace='divein')),
)
