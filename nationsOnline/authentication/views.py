from django.contrib.auth import get_user_model
from django.http import Http404

from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from authentication.serializers import UserSerializer, UserNationSerializer

class UserList(APIView):
    """
    GET: get all users and info about them
    POST: Create a new user
    """
    def get(self, request):
        """ Get all users """
        users = get_user_model().objects.all()
        serializer = UserNationSerializer(users, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        """ Create a User """ 
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    """
    GET: get a user's username and nation
    """
    def get(self, request, pk):
        """ Get a user's name and nation """
        try:
            user = get_user_model().objects.get(id=pk)
        except:
            return Http404
        serializer = UserNationSerializer(user, context={'request': request})
        return Response(serializer.data)

class UserLogin(APIView):
    """
    GET: check to see if the user's login credentials are correct or not
    """
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        return Response(None, status=status.HTTP_200_OK)