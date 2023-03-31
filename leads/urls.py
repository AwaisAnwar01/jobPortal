from django.urls import path
from .views import JobView



urlpatterns = [
  #  path('jobs/', JobView.as_view(), name='job_list'),
    path('jobs/', JobView.as_view(), name='job_list'),


]

