from django.contrib import admin
from django.urls import path
from . import views

app_name = 'shows'

urlpatterns = [
   path('editMovie/<slug:slug>/', views.editMovieDetails, name ="editMovieDetails"),
   path('editMovieList/', views.editMovieList, name="editMovie"),
   path('addNewMovie', views.addNewMovie, name="addNewMovie"),
   path('', views.show_list, name="list"),
]