from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import myUser


class registrationForm(UserCreationForm):

  class Meta:
    model=myUser
    fields= ("username", "first_name", "last_name", "email", "role")