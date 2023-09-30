from django.db import models
from django.contrib.auth.models import AbstractUser


class Skisubuser(AbstractUser):
    
    phone=models.CharField(max_length=14)
    created_date=models.DateField(auto_now_add=True)
    updated_date=models.DateField(auto_now=True)
    # status=models.CharField(max_length=20,default='Pending')
    is_active=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_user=models.BooleanField(default=False),
    is_admin=models.BooleanField(default=False)
    # def __str__(self):
    #   return self.name