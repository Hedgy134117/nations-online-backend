from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import User
from nations.serializers import NationSerializer

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'], 
            password=validated_data['password']
        )
        user.save()

        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

class UserNationSerializer(serializers.ModelSerializer):
    nation = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='nations:nation-detail')

    class Meta:
        model = User
        fields = ['id', 'username', 'nation']