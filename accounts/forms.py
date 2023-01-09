from django import forms
from . import models

class addNewUser(forms.ModelForm):
  class Meta:
    model = models.User
    fields = ['username, password, firstname, lastname, email, userRole, managerValidated']
