#from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import JobPortal
from .serializers import JobPortalSerializer,SavedJobsSerializer
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema,OpenApiParameter
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated
#from rest_framework.exceptions import PermissionDenied
from .models import Saved_Jobs
#from django.contrib.auth.models import User

# Create your views here.

class JobView(RetrieveUpdateDestroyAPIView, CreateAPIView):
    queryset = JobPortal.objects.all()
    serializer_class = JobPortalSerializer
    permission_classes = [IsAuthenticated]



    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset() 
        #current_user = self.request.user
       # queryset = queryset.filter(user=current_user)
        serialize_data = self.serializer_class(queryset, many = True)
        return Response(serialize_data.data, status=status.HTTP_200_OK)
    

    def post(self, request, *args, **kwargs):
        user = request.user
        if not request.user.is_company:
            return Response({'detail': 'Only companies can post jobs.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = self.serializer_class(data=request.data, context={'request': request, 'user': user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

    @method_decorator(extend_schema(
        parameters=[
            OpenApiParameter(name='id',
                             description='ID of the job',
                             required=True, type=str),
        ]
    ))

    def delete(self, request, *args, **kwargs):
        id = self.request.query_params.get("id")
        job = JobPortal.objects.filter(id = id)

        if not job:
            return Response("Not Found", status=status.HTTP_404_NOT_FOUND)
        job.delete()
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
        instance = JobPortal.objects.filter(id=id).first()

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
        instance = JobPortal.objects.filter(id=id).first()

        if not instance:
            return Response("Not Found", status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("Updated", status=status.HTTP_200_OK)
    

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