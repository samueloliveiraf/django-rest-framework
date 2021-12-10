from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Profile


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name',
            'email',
            'username',
            'password',
        ]   
        
        
class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        exclude = [
            'user'
        ] 

