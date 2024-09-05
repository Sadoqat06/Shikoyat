from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import *
from .forms import ShikoyatForm

def home_view(request):
    return render(request, 'home.html')

def Shkoyat(request):
    if request.method == 'POST':
        form = ShikoyatForm(request.POST)
        if form.is_valid():
            form.save()
            return render('home')
    else:
        form = ShikoyatForm()
    return render(request, 'Shkoyat.html', {'form': form})


def get_shikoyat(request):
    if request.method == 'POST':
        form = NomeroForm(request.POST)
        if form.is_valid():
            nomer = form.cleaned_data['telnomer']
            response = Shikoyat.objects.filter(telnomer=nomer)
            return render(request, 'Shikoyat.html', {'response': response})
    else:
        form = NomeroForm()
    return render(request, 'get_shikoyat.html', {'form': form})


def get_status(request, id):
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            telnomer = form.cleaned_data['telnomer']
            shikoyat = Shikoyat.objects.get(telnomer=telnomer, id = id)
            shikoyat.status = form.cleaned_data['status']
            shikoyat.save()
            return render(request, 'get_status.html', {'form': form})
        
        
        
        