from email.policy import default
from django.db import models

class City(models.Model):
    name = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.name

class Street(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.city}: {self.name}"

class Shop(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    street = models.ForeignKey(Street, on_delete=models.SET_NULL, null=True)
    house = models.SmallIntegerField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return f"{self.name} по адрессу {self.street} - {self.house}. Работает с {self.opening_time} до {self.closing_time}"

