from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewBookout
from .models import Logsheet, Pilots


# Create your views here.
from django.http import HttpResponse
from .models import Logsheet

def home(request):
    logsheet = Logsheet.objects.all()
    return render(request, 'home.html', {'logsheet': logsheet})

def logbook(request):
    logsheet = Logsheet.objects.all()
    return render(request, 'logbook.html', {'logsheet': logsheet})

def bookout(request):
    bookout = NewBookout()
    #board = get_object_or_404(Logsheet)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewBookout(request.POST)
        if form.is_valid():
            logsheet = form.save(commit=False)
            logsheet.starter = user
            logsheet.save()
            #post = Post.objects.create(
            #    message=form.cleaned_data.get('message'),
            #    topic=topic,
            #    created_by=user
            #)
            return redirect('logbook')  # TODO: redirect to the created topic page
    else:
        form = NewBookout()
    return render(request, 'bookout.html', {'bookout': bookout, 'form': form})

def bookin(request):
    bookin = NewBookin()
    #board = get_object_or_404(Logsheet)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewBookin(request.POST)
        if form.is_valid():
            logsheet = form.save(commit=False)
            logsheet.starter = user
            logsheet.save()
            #post = Post.objects.create(
            #    message=form.cleaned_data.get('message'),
            #    topic=topic,
            #    created_by=user
            #)
            return redirect('logbook')  # TODO: redirect to the created topic page
    else:
        form = NewBookin()
    return render(request, 'bookin.html', {'bookin': bookin, 'form': form})