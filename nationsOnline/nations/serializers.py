from rest_framework import serializers
from .models import *

# ---------- MAP ---------- # 

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

# ---------- GOVERNMENT ---------- # 

class GovernmentBoostSerializer(serializers.ModelSerializer):
    class Meta:
        model = GovernmentBoost
        fields = ['resource', 'percentage']

class GovernmentSerializer(serializers.ModelSerializer):
    boosts = GovernmentBoostSerializer(many=True, read_only=True, source='governmentboost_set')

    class Meta:
        model = Government
        fields = ['name', 'populationRate', 'boosts']

# ---------- MILITARY ---------- #

class TroopInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TroopInfo

class TroopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Troop

# ---------- BUILDING ---------- #

class ResourceBuildingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceBuildingInfo
        fields = '__all__'

class MilitaryBuildingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilitaryBuildingInfo
        fields = '__all__'

class ResourceBuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceBuilding
        fields = '__all__'

class MilitaryBuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilitaryBuilding
        fields = '__all__'

# ---------- NATION ---------- # 

class NationSerializer(serializers.ModelSerializer):
    resourceBuildings = ResourceBuildingSerializer(many=True, read_only=True, source='resourcebuilding_set')
    militaryBuildings = MilitaryBuildingSerializer(many=True, read_only=True, source='militarybuilding_set')

    class Meta:
        model = Nation
        fields = '__all__'

class ResourceBoostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceBoost
        fields = '__all__'