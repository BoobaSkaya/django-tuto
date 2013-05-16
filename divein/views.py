from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from divein.models import Diver,Level

class DiverListView(generic.ListView):
    model = Diver

class DiverDetailView(generic.DetailView):
    model = Diver