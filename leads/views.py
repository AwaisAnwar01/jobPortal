from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import JobPortal
from .serializers import JobPortalSerializer
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema,OpenApiParameter
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated
#from django.contrib.auth.models import User

# Create your views here.

class JobView(RetrieveUpdateDestroyAPIView, CreateAPIView):
    queryset = JobPortal.objects.all()
    serializer_class = JobPortalSerializer
    permission_classes = [IsAuthenticated]



    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serialize_data = self.serializer_class(queryset, many = True)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

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

   

