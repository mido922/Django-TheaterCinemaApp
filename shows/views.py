from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import newShow
from django.contrib.auth.decorators import login_required
from . import forms
from django.shortcuts import get_object_or_404
import re
from .models import reservation
from string import Template


# Create your views here.

def show_list(request):
  shows = newShow.objects.all().order_by('startTime',)
  return render(request, 'availableShows.html', {'shows':shows})


def addNewMovie(request):
  print(request)
  if request.method == 'POST':
    form = forms.addNewShow(request.POST, request.FILES)
    if form.is_valid():
      instance = form.save(commit=False)
      instance.slug = instance.title.lower().replace(" ", "-")
      
      instance.save()
      return redirect('shows:list')
    else:
      return render(request, 'addNewMovie.html')

  else:
    form = forms.addNewShow()
    # field = form.fields['slug']
    # field.widget = field.hidden_widget()
  return render(request, 'addNewMovie.html', {'form':form})


def editMovieList(request):
  shows = newShow.objects.all().order_by('date',)
  return render(request, 'editMovieList.html', {'shows':shows})


def editMovieDetails(request,slug):
  if request.method == 'POST':
    form = forms.addNewShow(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('shows:list')
  else:
    movie = newShow.objects.get(slug=slug)
    form = forms.addNewShow(instance=movie)
    return render(request, 'editMovieDetails.html', {'movie':movie,'form':form})


def checkMovieDetails(request,slug):
  movie = newShow.objects.get(slug=slug)
  reservations = reservation.objects.filter(title=slug)

  x=1
  if movie.screeningRoom==1:
    totalSeats = x*20
  else:
    totalSeats = x*30

  seatList = enumerate(["0"] * totalSeats, start=1)
  seatDiagram = []

  print(seatDiagram)

  for i in seatList:
    occupiedSeat=False
    print("checking seat")
    print(i[0])
    for j in reservations:
      if j.seatNumber == i[0]:
        print(":occupied")
        occupiedSeat=True
    if occupiedSeat==True:
      seatDiagram.append("Full Seat")
    else:
      seatDiagram.append("Empty Seat")

  print (seatDiagram)

  return render(request, 'checkMovieDetailscopy.html', {'seatDiagram':seatDiagram, 'movie':movie, 'totalSeats':range(totalSeats)})

def reserveASeat(request, seatCode, slug):
  if request.method == 'POST':
    username = request.user
    movie = newShow.objects.get(slug=slug)
    movieStartTime=movie.startTime
    movieTitle=movie.title
    print(seatCode, slug)

    rejectedapplication = 0
    reservations = reservation.objects.filter(title=slug)

    for j in reservations: 
      print("Checking a reservation with seat number ")
      print(j.seatNumber)
      if j.seatNumber == seatCode:
        rejectedapplication = 1

    if rejectedapplication == 0:
      reservation.objects.create(seatNumber=seatCode, title=movieTitle,reservee=username,startTime=movieStartTime)
    else:
      return render(request, 'errorPage.html', {})

    return redirect('shows:yourReservations')
  else:
    movie = newShow.objects.get(slug=slug)
    return render(request, 'seatDetails.html', {'seatCode': seatCode, 'movie':movie})

def yourReservations(request):
  username = request.user
  reservations = reservation.objects.filter(reservee=username)
  return render(request, 'yourReservations.html', {'reservations': reservations})

def errorPage(request):
  return render(request, 'errorPage.html', {})




# Screening Room 1 is 20 seats
# Screening Room 2 is 30 seats

# Add a credit card page for reserving a seat and check if the seat is already occupied at checkout - Done for adding of a new reservation, not added for credit or for verify occupied
# Add a list of the user's current reservations - DONE
# Add a button to cancel a reservation IF the time until the movie starts is more than 3 hours
# Fix editing features
# Search movies