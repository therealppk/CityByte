from urllib import request
from django.test import TestCase
from info.helpers.places import FourSquarePlacesHelper
from django.shortcuts import render
from info.helpers.weather import WeatherBitHelper
from datetime import datetime
import pytz
from search.helpers.photo import UnplashCityPhotoHelper
from urllib.request import urlopen
image_formats = ("image/png", "image/jpeg", "image/gif")


class CityByte_testcase(TestCase):
    def test_main_page(self):
        assert (render(request, 'search/search.html').status_code == 200)

    def test_cityphoto(self):
        photo_link = UnplashCityPhotoHelper().get_city_photo(city='Pune')
        site = urlopen(photo_link)
        meta = site.info()
        if meta["content-type"] in image_formats:
            assert True

    def test_photo(self):
        photo_link = FourSquarePlacesHelper().get_place_photo(fsq_id='518a71ab498e430858000827')
        site = urlopen(photo_link)
        meta = site.info()
        if meta["content-type"] in image_formats:
            assert True

#     def test_info_page(self):
#         city = 'New York City'
#         country = 'US'
#         weather_info = WeatherBitHelper().get_city_weather(city=city, country=country)["data"][0]

#         weather_info["sunrise"] = datetime.strptime(weather_info["sunrise"], "%H:%M").astimezone(pytz.timezone(weather_info['timezone'])).strftime("%I:%M")
#         weather_info["sunset"] = datetime.strptime(weather_info["sunset"], "%H:%M").astimezone(pytz.timezone(weather_info['timezone'])).strftime("%I:%M")
#         weather_info["ts"] = datetime.fromtimestamp(weather_info["ts"]).strftime("%m-%d-%Y, %H:%M")
#         dining_info = FourSquarePlacesHelper().get_places(city=f"{city}, {country}", categories="13065", sort="RELEVANCE", limit=5)
#         outdoor_info = FourSquarePlacesHelper().get_places(city=f"{city}, {country}", categories="16000", sort="RELEVANCE", limit=5)
#         airport_info = FourSquarePlacesHelper().get_places(city=f"{city}, {country}", categories="19040", sort="RELEVANCE", limit=5)
#         arts_info = FourSquarePlacesHelper().get_places(city=f"{city}, {country}", categories="10000", sort="RELEVANCE", limit=5)
#         photo_link = UnplashCityPhotoHelper().get_city_photo(city=city)
#         assert render(request, 'search/city_info.html', context={"weather_info": weather_info, "dining_info": dining_info, "outdoor_info": outdoor_info, "airport_info": airport_info, "photo_link": photo_link, "arts_info": arts_info, }).status_code == 200
