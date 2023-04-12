from django.db import models
from django.conf import settings
from users.models import User


# Create your models here.
class JobPortal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length= 100)
    description = models.CharField(max_length= 100)
    is_company = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Job Creation Time")
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name="Job Updation Time")



class Saved_Jobs(models.Model):
   user = models.ForeignKey(User,  on_delete=models.CASCADE)
   jobs = models.ForeignKey(JobPortal,  on_delete=models.CASCADE)
   title = models.CharField(max_length=100)
   description = models.CharField(max_length=100)
   created_at = models.DateTimeField(auto_now_add=True, verbose_name="Job Creation Time")
   updated_at = models.DateTimeField(auto_now=True, verbose_name="Job Updation Time")