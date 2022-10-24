# from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import HttpResponseBadRequest

from shops.models import City, Street, Shop
from shops.serializers import CitySerializer, ShopSerializer, StreetSerializer


class CityListView(APIView):

    def get(self, request, format=None):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response({"cities" :serializer.data})


class CityDetailView(APIView):

    def get(self,request, pk, format=None):
        try:
            city = City.objects.get(id = pk)
            streets = Street.objects.filter(city=city)
            serializer = StreetSerializer(streets, many=True)
            return Response({"streets": serializer.data})
        except City.DoesNotExist:
            return HttpResponseBadRequest()


class ShopView(APIView):
    def post(self, request):
        shop = request.data.get('shop')
        city = CitySerializer(data = shop.get('city'))
        street = StreetSerializer(data =shop.get('street'))
        if city.is_valid(raise_exception=True):
            shop['city'] = city.data
        if street.is_valid(raise_exception=True):
            shop['street'] = street.data
        serializer = ShopSerializer(data=shop)
        if serializer.is_valid(raise_exception=True):
            shop_saved = serializer.save()
        return Response({"success": "Shop '{}' created successfully".format(shop_saved.name)})

    def get(self, request):
        shops = Shop.objects.all()
        serializer = ShopSerializer(shops, many=True)
        return Response({"shops": serializer.data})
