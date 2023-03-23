from django.contrib import admin
from .models import JobPortal
# Register your models here.


# class JobPortaladmin(admin.ModelAdmin):
#     list_display = [ ]
    
admin.site.register(JobPortal)