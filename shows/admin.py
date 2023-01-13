from django.contrib import admin
from .models import newShow
from .models import reservation

# Register your models here.

admin.site.register(newShow)
admin.site.register(reservation)