from rest_framework import serializers

from .models import City, Street, Shop


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']


class StreetSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField(many=False)

    class Meta:
        model =  Street
        fields = ['id', 'name', 'city']


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['__all__']

