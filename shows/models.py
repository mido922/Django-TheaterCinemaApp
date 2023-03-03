from django.db import models
from django.contrib.auth.models import User
import datetime

screeningRoomChoices = (
  ('1', '1'),
  ('2', '2')
)

class newShow(models.Model):

  class screeningRoomChoices(models.IntegerChoices):
        Room1 = 1
        Room2 = 2

  title = models.CharField(max_length=100,default="untitled")
  slug = models.SlugField(default="")
  startTime= models.DateTimeField(default="1970-01-01 00:00:00")
  endTime = models.DateTimeField(default="1970-01-01 00:00:00")
  cancelTime = models.DateTimeField(default="1970-01-01 00:00:00")
  description = models.TextField(default="To Be Filled")
  posterImage = models.ImageField(default='default.png')
  screeningRoom = models.IntegerField(choices=screeningRoomChoices.choices, default='0')

  def __str__(self):
    return self.title


class reservation(models.Model):

  now = datetime.datetime.now()

  title = models.CharField(max_length=100,default="untitled")
  seatNumber = models.IntegerField(default = 0)
  reservee = models.CharField(max_length=100,default="untitled")
  startTime = models.DateTimeField(default="1970-01-01 00:00:00")
  cancelTime = models.DateTimeField(default="1970-01-01 00:00:00")

  def __str__(self):
    reservationName = self.title + ": Seat " + str(self.seatNumber)
    return reservationName