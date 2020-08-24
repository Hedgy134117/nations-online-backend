from django.contrib.auth import get_user_model
from django.http import Http404

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

class BuildingList(APIView):
    """
    GET: Get all building options
    """

    def get(self, request):
        rBuildings = ResourceBuildingInfo.objects.all()
        mBuildings = MilitaryBuildingInfo.objects.all()
        rSerializer = ResourceBuildingInfoSerializer(rBuildings, many=True)
        mSerializer = MilitaryBuildingInfoSerializer(mBuildings, many=True)
        response = {
            'resourceBuildings': rSerializer.data,
            'militaryBuildings': mSerializer.data,
        }
        return Response(response)

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

class NationDetail(APIView):
    """
    GET: get all the info about a nation
    PATCH: edit a nation's info
    """
    # allow get without auth, but put needs auth
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_nation(self, pk):
        try:
            return Nation.objects.get(id=pk)
        except:
            return Http404

    def get(self, request, pk):
        """ Get a nation's information """
        nation = self.get_nation(pk=pk)
        serializer = NationSerializer(nation)
        return Response(serializer.data)
    
    def patch(self, request, pk):
        """ Edit a nation's informaion """
        nation = self.get_nation(pk=pk)
        if nation.owner != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = NationSerializer(nation, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors)