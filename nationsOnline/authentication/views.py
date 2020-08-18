from rest_framework import permissions
from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

class CreateUser(generics.CreateAPIView):
    model = get_user_model
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer

class ListUser(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UserSerializer