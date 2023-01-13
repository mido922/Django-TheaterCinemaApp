from django import forms
from . import models

class addNewShow(forms.ModelForm):
  class Meta:
    model = models.newShow
    fields = ['title', 'description', 'date', 'posterImage', 'startTime', 'endTime', 'screeningRoom']

    # widgets = {
    #   'slug': forms.TextInput(attrs={'type': 'hidden'}),
    # }