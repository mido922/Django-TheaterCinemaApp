from django.contrib import admin
from .models import managerUser
from .models import customerUser

# Register your models here.

admin.site.register(managerUser)
admin.site.register(customerUser)