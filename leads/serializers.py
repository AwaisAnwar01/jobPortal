from .models import JobPortal
# job serializer 

from rest_framework import serializers
from .models import JobPortal

class JobPortalSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = JobPortal
        fields = ['id', 'title', 'description', 'posted_by', 'created_at', 'updated_at']