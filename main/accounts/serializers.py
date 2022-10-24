from dataclasses import field, fields
from pyexpat import model
from urllib import request
from rest_framework import serializers

from main import settings
from .models import CustomUser,Roles,UserActivities


class CreateUserSerializers(serializers.Serializer):
    email = serializers.EmailField()
    fullname = serializers.CharField()
    role= serializers.ChoiceField(Roles)

class LoginSerializer (serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(request=False)
    is_new_user = serializers.BooleanField(default=False,required=False)

class UpdatePassowrdSerializer(serializers.ModelSerializer):
    class Meta:
        model= CustomUser
        exclude = ("password",)





class UserActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model= UserActivities
        fields = ("__all__")