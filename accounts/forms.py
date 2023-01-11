from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class registrationForm(UserCreationForm):

  CHOICES = (
      ("customer", 'Customer'),
      ("manager", 'Manager'),
  )

  username = forms.CharField(max_length=100, required=True),
  password1 = forms.CharField(max_length=100, required=True),
  password2 = forms.CharField(max_length=100, required=True),
  first_name = forms.CharField(max_length=100, required=True),
  last_name = forms.CharField(max_length=100, required=True),
  email = forms.EmailField(max_length=100,required=True)
  role = forms.ChoiceField(required=True, choices=CHOICES)
