from rest_framework import serializers
from .models import Biome, Region

class BiomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biome
        fields = ['name']

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['biome', 'name']