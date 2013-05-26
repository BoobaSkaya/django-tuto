from django.shortcuts import get_object_or_404, render
from django.views import generic

from django.contrib.auth import logout
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from datetime import datetime

from divein.models import Diver,Dive,DivePart,Spot,Club
from divein.forms  import DiveForm, DiveForm2

def index(request):
    dives = Dive.objects.all()
    return render(request, 'divein/index.html', {'dives': dives})

class DiverListView(generic.ListView):
    model = Diver

class DiverDetailView(generic.DetailView):
    model = Diver

class SpotDetailView(generic.DetailView):
    model = Spot

class SpotListView(generic.ListView):
    model = Spot

@login_required(login_url='/divein/login')
def dive_detail(request, pk):
    dive 		= get_object_or_404(Dive, pk=pk)
    tags 		= dive.tags.all()
    dive_parts 	= DivePart.objects.filter(dive=dive)
    return render(request, 'divein/dive_detail.html', {'dive': dive, 'tags' : tags, 'dive_parts' : dive_parts})

@login_required(login_url='/divein/login')
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

@login_required(login_url='/divein/login')
def spot_add_dive(request, pk):
    """
    Adds a dive to an existing spot
    """
    spot  = get_object_or_404(Spot, pk=pk)
    if request.method == 'POST': # If the form has been submitted...
        form = DiveForm2(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            max_deep = form.cleaned_data['max_deep']
            length   = form.cleaned_data['length']
            time     = form.cleaned_data['time']   
            date     = form.cleaned_data['date']
            print('date is {} \ntime is {}'.format(date, time))
            #Create a new Dive
            d = Dive(
                date = datetime.combine(date, time),
                duration = length,
                depth      = max_deep,
                club        = get_object_or_404(Club, pk=1),
                spot        = spot,
                created_by  = request.user.diver,
                created_date = date.today(),
            )
            d.save()


            return HttpResponseRedirect('/divein/dive/{}'.format(d.id)) # Redirect after POST to created dive
    else:
        form = DiveForm2()
    return render(request, 'divein/spot_add_dive.html', {
        'form' : form,
        'spot' : spot,
    })


@login_required(login_url='/divein/login')
def profile(request):
    return render(request, 'divein/profile.html', {'gravatar' : request.user.diver.getGravatar(100)})

#Do not use logout bu logoutv to avoid infinite loop
@login_required(login_url='/divein/login')
def logoutv(request):
    logout(request)
    return render(request, 'divein/index.html')
