from django.urls import path

from weather import views

urlpatterns = [
    path('weather/', views.getWeatherPage, name='weather')
]
