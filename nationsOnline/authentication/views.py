from django.contrib.auth import get_user_model

from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from authentication.serializers import UserSerializer

class UserList(APIView):
    """
    GET: get all users and info about them
    POST: Create a new user
    """
    def get(self, request):
        """ Get all users """
        users = get_user_model().objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        """ Create a User """ 
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)