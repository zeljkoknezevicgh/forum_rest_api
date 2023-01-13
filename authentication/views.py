from django.shortcuts import render
from rest_framework import generics

from authentication.models import User
from authentication.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

