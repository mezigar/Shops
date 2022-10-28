from rest_framework.test import APITestCase
from rest_framework.status import HTTP_200_OK
from shops.models import City
from shops.serializers import CitySerializer

class GetCityApiTestCase(APITestCase):
    def test_get_city(self):
        city_1 = City.objects.create(name='Test city 1')
        city_2 = City.objects.create(name='Test city 2')
        url = "http://127.0.0.1:8000/city/?format=json"
        response = self.client.get(url)
        serializer_data = CitySerializer([city_1, city_2], many=True).data 
        self.assertEqual(HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data['cities'])