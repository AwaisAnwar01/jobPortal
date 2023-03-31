from rest_framework import serializers
#from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .models import User
#user =  get_user_model()


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["password", "username"]

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = User.objects.create(**validated_data)
        return user

#Register Serializer

class RegisterSerializer(serializers.ModelSerializer):
     class Meta:
         model = User
         fields = ('id', 'username', 'email', 'password')
         extra_kwargs = {'password': {'write_only': True}}

     def create(self, validated_data):
         validated_data['password'] = make_password(validated_data['password'])
         user = User.objects.create(**validated_data)
         return user


class ChangePasswordSerializer(serializers.Serializer):
    

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)