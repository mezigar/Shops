from django.urls import path
from rest_framework.routers import SimpleRouter

from shops import views

urlpatterns = [
    path('', views.CityList.as_view()),
    path('city/<int:pk>/street/', views.CityDetail.as_view()),
]