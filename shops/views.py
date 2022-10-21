# from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework  import status
from django.http import HttpResponseBadRequest
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
        try:
            city = City.objects.get(id = pk)
            streets = Street.objects.filter(city=city)
            serializer = StreetSerializer(streets, many=True)
            return Response(serializer.data)
        except City.DoesNotExist:
            return HttpResponseBadRequest()