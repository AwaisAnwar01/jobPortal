from django.urls import path
from .views import JobView



urlpatterns = [
    path('jobs/', JobView.as_view(), name='job_list'),
    path('jobs/delete/<int:pk>', JobView.as_view(), name="delete job"),
    path('jobs/update/<int:pk>', JobView.as_view(), name="update job")

]
