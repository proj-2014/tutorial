#from django.shortcuts import render

# Create your views here.

# quickstart/views.py
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    query and edit user 's  API endpoint
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    query and edit group 's API endpoint
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer