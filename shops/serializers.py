from rest_framework import serializers

from .models import City, Street, Shop


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']


class StreetSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model =  Street
        fields = ['id', 'name', 'city']

    def create(self, validated_data):
        city_data = validated_data.pop('city')
        city = City.objects.get_or_create(**city_data)
        street = Street.objects.get_or_create(**validated_data)
        street.city.add(city)


class ShopSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    street = StreetSerializer()

    class Meta:
        model = Shop
        fields = ['id', 'name', 'city', 'street', 'house', 'opening_time', 'closing_time']

    def create(self, validated_data):
        city_data = validated_data.get('city')
        city = City.objects.get_or_create(name=city_data['name'])
        street_data = validated_data.get('street')
        street = Street.objects.get_or_create(name=street_data['name'], city=city[0]) 
        shop = Shop.objects.create(
            name=validated_data['name'],
            city=city[0],
            street=street[0],
            house=validated_data['house'],
            opening_time=validated_data['opening_time'],
            closing_time=validated_data['closing_time'])
        return shop
        
