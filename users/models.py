from django.db import models
from django.contrib.auth.models import AbstractUser
from common.models import TimeStampedModel


class User(TimeStampedModel, AbstractUser,models.Model):
        is_company = models.BooleanField(default=False)
        staff = models.BooleanField(null=True, default=None)
       
     


   

