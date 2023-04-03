from django.db import models

from django.conf import settings


# Create your models here.
# Create your models here.
class JobPortal(models.Model):
    title = models.CharField(max_length= 100)
    description = models.CharField(max_length= 100)
    posted_by = models.CharField (max_length= 100)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Job Creation Time")
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name="Job Updation Time")







