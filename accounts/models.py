from django.db import models
from django.contrib.auth.models import  AbstractUser



userRoleChoices = (
  ('manager', 'manager'),
  ('customer', 'customer')
)

# Create your models here.
class managerUser(AbstractUser):
  user= models.OneToOneField(User,on_delete=models.CASCADE)
  userRole= models.CharField(max_length= 100, choices=userRoleChoices, default='customer')
  managerValidated = models.BooleanField(default=False)

class customerUser(AbstractUser):
  user= models.OneToOneField(User,on_delete=models.CASCADE)
  userRole= models.CharField(max_length= 100, choices=userRoleChoices, default='customer')


# python3 manage.py makemigrations
# python3 manage.py migrate
