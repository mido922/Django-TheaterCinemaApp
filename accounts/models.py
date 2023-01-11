from django.db import models
from django.contrib.auth.models import  AbstractUser, User




# Create your models here.

class myUser(AbstractUser):
  pass

  CHOICES = (
      ("customer", 'Customer'),
      ("manager", 'Manager'),
  )
  
  role = models.ChoiceField(required=True, choices=CHOICES)
  managerValidated = models.BooleanField(default=False)


# python3 manage.py makemigrations
# python3 manage.py migrate
