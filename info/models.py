from django.db import models

class CitySearchRecord(models.Model):
    city_name = models.CharField(max_length=126)
    country_name = models.CharField(max_length=126)
    
    def __str__(self):
        return f"{self.city_name}-{self.country_name}"