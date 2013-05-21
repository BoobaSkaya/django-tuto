from django.shortcuts import get_object_or_404, render
from django.views import generic
from divein.models import Diver,Dive, DiveForm,DivePart,Spot
from django.contrib.auth import logout
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
import datetime


def index(request):
    dives = Dive.objects.all()
    return render(request, 'divein/index.html', {'dives': dives})

class DiverListView(generic.ListView):
    model = Diver

class DiverDetailView(generic.DetailView):
    model = Diver

class SpotDetailView(generic.DetailView):
    model = Spot

def dive_detail(request, pk):
    dive 		= get_object_or_404(Dive, pk=pk)
    tags 		= dive.tags.all()
    dive_parts 	= DivePart.objects.filter(dive=dive)
    return render(request, 'divein/dive_detail.html', {'dive': dive, 'tags' : tags, 'dive_parts' : dive_parts})

def dive_form(request):
    if request.method == 'POST': # If the form has been submitted...
        form = DiveForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            form.save()
            return HttpResponseRedirect('/divein') # Redirect after POST to HOME
    else:
        form = DiveForm(initial = {'created_by' : request.user, 'created_date' : datetime.date.today})
    return render(request, 'divein/dive_form.html', {
        'form': form,
    })


def profile(request):
    return render(request, 'divein/profile.html', {'gravatar' : request.user.diver.getGravatar(100)})

#Do not use logout bu logoutv to avoid infinite loop
def logoutv(request):
    logout(request)
    return render(request, 'divein/index.html')
