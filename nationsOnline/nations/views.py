from django.contrib.auth import get_user_model

from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from nations.models import *
from nations.serializers import *

# Create your views here.
class BiomeList(APIView):
    """
    GET: Get a list of biomes
    """
    def get(self, request):
        """ Get all biomes """
        biomes = Biome.objects.all()
        serializer = BiomeSerializer(biomes, many=True)
        return Response(serializer.data)

class RegionList(APIView):
    """
    GET: Get a list of regions
    """
    def get(self, request):
        """ Get all regions """
        regions = Region.objects.all()
        serializer = RegionSerializer(regions, many=True)
        return Response(serializer.data)

class GovernmentList(APIView):
    """
    GET: Get a list of governments
    """
    def get(self, request):
        """ Get all governments """
        governments = Government.objects.all()
        serializer = GovernmentSerializer(governments, many=True)
        return Response(serializer.data)

class NationList(APIView):
    """
    GET: get all nations
    POST: create a new nation
    """

    # allow get without auth, but post needs auth
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        """ Get all nations """
        nations = Nation.objects.all()
        serializer = NationSerializer(nations, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """ Create a new nation """
        serializer = NationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)