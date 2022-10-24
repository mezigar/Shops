from django.urls import path
from rest_framework.routers import SimpleRouter

from shops import views

urlpatterns = [
    path('', views.CityListView.as_view()),
    path('<int:pk>/street/', views.CityDetailView.as_view()),
]