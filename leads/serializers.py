from .models import JobPortal
# job serializer 
from rest_framework import serializers
from .models import JobPortal
from .models import Saved_Jobs

class JobPortalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JobPortal
        fields = ['id','title', 'description', 'created_at', 'updated_at','is_company']
        read_only_fields = ['id','user']
    
    '''
    def create(self, validated_data):
        user = self.context['request'].user
        
        if not user.is_company:
            raise serializers.ValidationError("Only companies can post jobs.")
        
        return JobPortal.objects.create(**validated_data)
    '''
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user_id'] = user.id  # add this line to set user_id
        return JobPortal.objects.create(**validated_data)
    


class SavedJobsSerializer(serializers.ModelSerializer):
    #  user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    #  jobs = serializers.PrimaryKeyRelatedField(queryset=JobPortal.objects.all())

     class Meta:
        model = Saved_Jobs
        fields = [ 'user', 'jobs', 'title', 'description', 'created_at', 'updated_at']
        read_only_fields = ['user']


  
    