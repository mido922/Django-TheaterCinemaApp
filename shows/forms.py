from django import forms
from . import models

class addNewShow(forms.ModelForm):
  class Meta:
    model = models.newShow
    fields = ['title', 'description', 'slug', 'date', 'posterImage', 'startTime', 'endTime', 'screeningRoom']