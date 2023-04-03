from .views import RegisterAPI
from .views import ChangePasswordView
from knox import views as knox_views
#from .views import LoginAPI
from django.urls import path
from .views import SavedJobsView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('saved-jobs/', SavedJobsView.as_view(), name='saved_jobs')
    


]