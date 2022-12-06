from django.urls import path

from .views import city_suggestions, city_photo

urlpatterns = [
    path("city", city_suggestions, name="city_search"),
    path("city/photo", city_photo, name="city_photo"),
]
