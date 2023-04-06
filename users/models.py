from django.contrib.auth.models import AbstractUser
from common.models import TimeStampedModel
from django.db import models

from leads.models import JobPortal

class User(TimeStampedModel, AbstractUser):
    pass
    
class Saved_Jobs(models.Model):
   user = models.ForeignKey(User,  on_delete=models.CASCADE)
   jobs = models.ForeignKey(JobPortal,  on_delete=models.CASCADE)
   title = models.CharField(max_length=100)
   description = models.CharField(max_length=100)
   created_at = models.DateTimeField(auto_now_add=True, verbose_name="Job Creation Time")
   updated_at = models.DateTimeField(auto_now=True, verbose_name="Job Updation Time")