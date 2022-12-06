from django.db import models
from django.contrib.auth import get_user_model


class CitySearchRecord(models.Model):
    city_name = models.CharField(max_length=126)
    country_name = models.CharField(max_length=126)

    def __str__(self):
        return f"{self.city_name}-{self.country_name}"


class Comment(models.Model):
    city = models.CharField(max_length=125)
    country = models.CharField(max_length=125)
    comment = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city}-{self.country}-{self.author.username}"


class FavCityEntry(models.Model):
    city = models.CharField(max_length=125)
    country = models.CharField(max_length=125)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.city}-{self.country}-{self.user.username}"
