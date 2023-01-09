from django.db import models
from django.contrib.auth.models import User

screeningRoomChoices = (
  ('1', '1'),
  ('2', '2')
)

class newShow(models.Model):

  class screeningRoomChoices(models.IntegerChoices):
        Room1 = 1
        Room2 = 2


  title = models.CharField(max_length=100,default="untitled")
  slug = models.SlugField(default="untitled")
  date = models.DateField(default= "1900")
  posterImage = models.ImageField(default='default.png')
  startTime = models.TimeField(default='00:00')
  endTime = models.TimeField(default='00:00')
  screeningRoom = models.IntegerField(choices=screeningRoomChoices.choices, default='0')

  def __str__(self):
    return self.title