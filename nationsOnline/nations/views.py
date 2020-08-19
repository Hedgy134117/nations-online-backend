from django.contrib.auth import get_user_model

from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from nations.models import Biome, Region
from nations.serializers import BiomeSerializer, RegionSerializer

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