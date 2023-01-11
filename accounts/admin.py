from django.contrib import admin
from .models import myUser
from .forms import registrationForm

# Register your models here.

admin.site.register(myUser)