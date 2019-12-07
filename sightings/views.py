from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Squirrel
from . forms import SquirrelForm

# Create your views here.

def all_squirrels(request):
    squirrels = Squirrel.objects.all()
    context = {
        'squirrels': squirrels,
    }
    return render(request, 'sightings/all.html', context)



def add_squirrel(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        # check data with form
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form = SquirrelForm()
    context = {
        'form': form,
    }
    return render(request, 'sightings/edit.html', context)



def edit_squirrel(request,squirrel_id):
    squirrel = Squirrel.objects.get(squirrel_id=squirrel_id)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
         form = SquirrelForm(instance=squirrel)

    context = {
                'form':form,
                }
    return render(request,'sightings/edit.html',context)

def stats(request):
    squirrels = Squirrel.objects.all()
    context = {
        'squirrels': squirrels,
    }
    return render(request, 'sightings/stats.html', context)

