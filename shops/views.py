# from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework  import status
from shops import serializers

from shops.models import City, Street
from shops.serializers import CitySerializer, StreetSerializer


class CityList(APIView):

    def get(self, request, format=None):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)


class CityDetail(APIView):

    def get(self,request, pk, format=None):
        city = City.objects.get(id = pk)
        # try except for DoesNotExist
        streets = Street.objects.filter(city=city)
        serializer = StreetSerializer(streets, many=True)
        # Name instead of id!
        return Response(serializer.data)

