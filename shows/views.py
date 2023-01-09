from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import newShow
from django.contrib.auth.decorators import login_required
from . import forms
from django.shortcuts import get_object_or_404

# Create your views here.

def show_list(request):
  shows = newShow.objects.all().order_by('date',)
  return render(request, 'availableShows.html', {'shows':shows})



def addNewMovie(request):
  if request.method == 'POST':
    form = forms.addNewShow(request.POST, request.FILES)
    if form.is_valid():
      #Save article to database
      instance = form.save(commit=False)
      instance.author = request.user
      instance.save()
      return redirect('shows:list')
  else:
    form = forms.addNewShow()
  return render(request, 'addNewMovie.html', {'form':form})

def editMovieList(request):
  shows = newShow.objects.all().order_by('date',)
  return render(request, 'editMovieList.html', {'shows':shows})

def editMovieDetails(request,slug):
  if request.method == 'POST':
    form = forms.addNewShow(request.POST, request.FILES)
    if form.is_valid():
      #Save article to database
      form.save()
      return redirect('shows:list')
  else:
    movie = newShow.objects.get(slug=slug)
    form = forms.addNewShow(instance=movie)
    return render(request, 'editMovieDetails.html', {'movie':movie,'form':form})
