from django.urls import path
from shops import views

urlpatterns = [
    path('city/', views.CityList.as_view()),
    path('city/<int:pk>/street/', views.CityDetail.as_view()),
]