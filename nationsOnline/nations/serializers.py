from rest_framework import serializers
from .models import *

class BiomeBoostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BiomeBoost
        fields = ['resource', 'percentage']

class BiomeSerializer(serializers.ModelSerializer):
    boosts = BiomeBoostSerializer(many=True, read_only=True, source='biomeboost_set')

    class Meta:
        model = Biome
        fields = ['name', 'boosts']


class RegionSerializer(serializers.ModelSerializer):
    biome = serializers.StringRelatedField(many=False)

    class Meta:
        model = Region
        fields = ['biome', 'name']

class GovernmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Government
        fields = '__all__'

class GovernmentBoostSerializer(serializers.ModelSerializer):
    class Meta:
        model = GovernmentBoost
        fields = '__all__'

class NationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nation
        fields = '__all__'

class ResourceBoostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceBoost
        fields = '__all__'