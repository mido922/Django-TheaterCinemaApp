from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


app_name = 'shows'

urlpatterns = [
   path('checkMovie/<slug:slug>/', views.checkMovieDetails, name ="checkMovieDetails"),
   path('editMovie/<slug:slug>/', views.editMovieDetails, name ="editMovieDetails"),
   path('editMovieList/', views.editMovieList, name="editMovie"),
   path('addNewMovie', views.addNewMovie, name="addNewMovie"),
   path('', views.show_list, name="list"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)