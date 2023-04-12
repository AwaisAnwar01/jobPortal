from django.urls import path
from .views import JobView,SavedJobsView





urlpatterns = [
    path('jobs/', JobView.as_view(), name='job_list'),
    path('saved-jobs/', SavedJobsView.as_view(), name='saved_jobs')
    
    
]

