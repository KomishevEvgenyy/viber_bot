from django.contrib.auth.models import User
from rest_framework import serializers

from .models import ViberUser


class ViberUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ViberUser
        fields = ['user']


#class GroupSerializer(serializers.HyperlinkedModelSerializer):
    #class Meta:
        #model = Group
        #fields = ['url', 'name']
