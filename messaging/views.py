from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from messaging.models import Message
from messaging.serializers import MessageSerializer



class MessageListCreateAPIView(generics.ListCreateAPIView):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)


    def get_queryset(self):
        logged_in_user = self.request.user
        queryset = super().get_queryset().filter(receiver=logged_in_user)
        return queryset

