from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import JobPortal
from .serializers import JobPortalSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class JobView(RetrieveUpdateDestroyAPIView, CreateAPIView):
    queryset = JobPortal.objects.all()
    serializer_class = JobPortalSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serialize_data = self.serializer_class(queryset, many = True)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)