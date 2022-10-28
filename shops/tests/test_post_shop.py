from collections import OrderedDict
from rest_framework.test import APITestCase
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from shops.models import City, Street, Shop
from shops.serializers import CitySerializer, StreetSerializer, ShopSerializer

import datetime
import json

class PostShopApiTestCase(APITestCase):
    def test_post_shops(self):
        city_1 = City.objects.create(name='Test city 1')
        city_2 = City.objects.create(name='Test city 2')
        street_1 = Street.objects.create(name = 'Test street 1', city = city_1)
        street_2 = Street.objects.create(name = 'Test street 2', city = city_1)
        url = "http://127.0.0.1:8000/shop/"
        shop_1 = {"shop": {
    "id": 1,
    "name": "Глобус",
    "city": {"name":"Рязань"},
    "street": {"name": "Быстрецкая", "city": {"name":"Рязань"}},
    "house": 2,
    "opening_time": "8:00",
    "closing_time": "22:00"
}
}
        response = self.client.post(url, shop_1, format='json')
        self.assertEqual(HTTP_200_OK, response.status_code)

        response = self.client.get(url)
        self.assertEqual(HTTP_200_OK, response.status_code)
        serializer_data = ShopSerializer(shop_1["shop"]).data
        self.assertEqual(OrderedDict(serializer_data), response.data['shops'])
