from django.shortcuts import get_object_or_404, render
from django.views import generic
from divein.models import Diver,Dive,DivePart,Spot

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
