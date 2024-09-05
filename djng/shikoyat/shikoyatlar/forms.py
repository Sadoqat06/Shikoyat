from django import forms
from .models import *

class ShikoyatForm(forms.ModelForm):
    class Meta:
        model = Shikoyat
        fields = '__all__'



class NomeroForm(forms.ModelForm):
    class Meta:
        model = Shikoyat
        fields = ['telnomer']
        

class EditForm(forms.ModelForm):
    class Meta:
        model = Shikoyat
        fields = ['status', 'telnomer']