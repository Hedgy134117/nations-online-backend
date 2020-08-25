from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
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
    def create(self, validated_data):
        costs = [
            [self.validated_data['nation'].food, self.validated_data['info'].foodCost],
            [self.validated_data['nation'].iron, self.validated_data['info'].ironCost],
            [self.validated_data['nation'].aluminum, self.validated_data['info'].aluminumCost],
            [self.validated_data['nation'].steel, self.validated_data['info'].steelCost],
            [self.validated_data['nation'].wood, self.validated_data['info'].woodCost],
            [self.validated_data['nation'].rawUranium, self.validated_data['info'].rawUraniumCost],
            [self.validated_data['nation'].enrichedUranium, self.validated_data['info'].enrichedUraniumCost],
            [self.validated_data['nation'].oil, self.validated_data['info'].oilCost],
        ]
        for values in costs:
            if values[0] < values[1]:
                print('error here')
                raise serializers.ValidationError('Insufficient Resources')
            elif values[0] >= values[1]:
                values[0] -= values[1]
        
        nation = Nation.objects.get(owner=self.validated_data['nation'].owner)
        nation.food = costs[0][0]
        nation.iron = costs[1][0]
        nation.aluminum = costs[2][0]
        nation.steel = costs[3][0]
        nation.wood = costs[4][0]
        nation.rawUranium = costs[5][0]
        nation.enrichedUranium = costs[6][0]
        nation.oil = costs[7][0]
        print('HELLO')
        nation.save()

        return ResourceBuilding.objects.create(**validated_data)

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