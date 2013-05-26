from divein.models import Dive
from django.forms import ModelForm
from django import forms
from datetime  import date,time,datetime

class DiveForm(ModelForm):
    class Meta:
        model = Dive
        #In the future, remove created_by and created_date
        #exclude = ('created_by', 'created_date') 
        # exclude m2m relation with through attribute. Don't know how to do it for now
        exclude = ('divers') 

class DiveForm2(forms.Form):
    max_deep    = forms.DecimalField(min_value=0, max_value=70)
    length      = forms.IntegerField(min_value=0, max_value=240)
    time        = forms.TimeField(initial=datetime.now().time())
    date        = forms.DateField(initial=date.today())
    
    pass
