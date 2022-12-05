from django.contrib import admin
from .models import CitySearchRecord, Comment, FavCityEntry


admin.site.register(CitySearchRecord)
admin.site.register(FavCityEntry)
admin.site.register(Comment)
