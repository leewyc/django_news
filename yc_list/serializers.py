from django.contrib.auth.models import  User,Group
from rest_framework import serializers
from .models import YcListViews

class ListSerializer(serializers.ModelSerializer):
    id = serializers.CharField(max_length=20)
    gtitle = serializers.CharField(max_length=20)
    gcontext = serializers.smart_text
    gpic = serializers.CharField(max_length=100)
    class Meta:
        model = YcListViews
        #fileds = ('id','gtitle','gcontext','gpic')
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email','groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url','name')


#class MeiziSerializer(serializer.ModelSerializer):
#    class Meta:
#        model = Meizis
#        fields = {}