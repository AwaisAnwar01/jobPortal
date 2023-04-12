from rest_framework import serializers
#from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .models import User

#user =  get_user_model()


# User Serializer(registerAPI)

class UserSerializer(serializers.ModelSerializer):
    is_company = serializers.BooleanField(default=False)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name',
                  'is_active', 'is_staff', 'is_superuser', 'password','is_company')
        read_only_fields = ('id', 'is_active', 'is_staff', 'is_superuser')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data : dict):
        validated_data['password'] = make_password(validated_data['password'])
        user = super().create(validated_data)
        return user


class ChangePasswordSerializer(serializers.Serializer):
    

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


