#from django.shortcuts import render
from users.serializers import UserSerializer
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated 
#from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import SavedJobsSerializer
from .models import Saved_Jobs
#from knox.auth import TokenAuthentication
from drf_spectacular.utils import extend_schema,OpenApiParameter
from django.utils.decorators import method_decorator
from .models import Saved_Jobs
# Create your views here.


# Register API



class RegisterAPI(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model()


    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,})
    




class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
    


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SavedJobsView(CreateAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = SavedJobsSerializer
    queryset = Saved_Jobs.objects.all()
    permission_classes = [IsAuthenticated]
   
    def post(self, request, *args, **kwargs):
        serializer =  SavedJobsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def get(self, request):
        current_user = request.user
        queryset = Saved_Jobs.objects.filter(user=current_user)
        serializer = SavedJobsSerializer(queryset, many=True)
        return Response(serializer.data)

    @method_decorator(extend_schema(
        parameters=[
            OpenApiParameter(name='id',
                             description='ID of the job',
                             required=True, type=str),
        ]
    ))

    def delete(self, request):
        id = self.request.query_params.get("id")
        Job = Saved_Jobs.objects.filter(user = request.user)

        if not Job:
            return Response("Not Found", status=status.HTTP_404_NOT_FOUND)
        Job.delete()
        return Response("Deleted", status=status.HTTP_200_OK) 
    

    @method_decorator(extend_schema(
        parameters=[
            OpenApiParameter(name='id',
                             description='ID of the job',
                             required=True, type=str),
        ]
    ))
    def put(self, request, *args, **kwargs):
        id = self.request.query_params.get("id")
        instance = Saved_Jobs.objects.filter(user = request.user).first()

        if not instance:
            return Response("Not Found", status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

   
    @method_decorator(extend_schema(
        parameters=[
            OpenApiParameter(name='id',
                             description='ID of the job',
                             required=True, type=str),
        ]
    ))

    def patch(self, request, *args, **kwargs):
        id = self.request.query_params.get("id")
        instance = Saved_Jobs.objects.filter(user = request.user).first()

        if not instance:
            return Response("Not Found", status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("Updated", status=status.HTTP_200_OK)