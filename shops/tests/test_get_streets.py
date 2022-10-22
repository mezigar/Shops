from rest_framework.test import APITestCase
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from shops.models import City, Street
from shops.serializers import CitySerializer, StreetSerializer

class GetStreetApiTestCase(APITestCase):
    def test_get_street(self):
        city_1 = City.objects.create(name='Test city 1')
        city_2 = City.objects.create(name='Test city 2')
        street_1 = Street.objects.create(name = 'Test street 1', city = city_1)
        street_2 = Street.objects.create(name = 'Test street 2', city = city_1)
        url1 = "http://127.0.0.1:8000/city/1/street/?format=json"
        response = self.client.get(url1)
        serializer_data = StreetSerializer([street_1, street_2], many = True).data
        self.assertEqual(HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

        url2 = "http://127.0.0.1:8000/city/2/street/?format=json"
        response2 = self.client.get(url2)
        self.assertEqual(HTTP_200_OK, response.status_code)
        self.assertEqual([], response2.data)

        url3 = "http://127.0.0.1:8000/city/3/street/?format=json"
        response3 = self.client.get(url3)
        self.assertEqual(HTTP_400_BAD_REQUEST, response3.status_code)