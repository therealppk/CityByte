from datetime import datetime

import pytz
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from info.helpers.places import FourSquarePlacesHelper
from info.helpers.weather import WeatherBitHelper
from search.helpers.photo import UnplashCityPhotoHelper
from .models import CitySearchRecord
from django.core.cache import cache


@require_http_methods(["GET"])
def place_photo(request):
    photo_link = FourSquarePlacesHelper().get_place_photo(fsq_id=request.GET.get('fsq_id'))
    print("PhotoLink",photo_link )
    return redirect(photo_link)


@require_http_methods(["GET"])
def info_page(request):
    city = request.GET.get("city")
    country = request.GET.get("country")
    
    if(CitySearchRecord.objects.filter(city_name=city, country_name=country).count() == 0):
        CitySearchRecord.objects.create(city_name=city, country_name=country)

    # try cache first
    weather_info = cache.get(f"{city}-weather")

    if not weather_info:
        try:
            weather_info = WeatherBitHelper().get_city_weather(city=city, country=country)["data"][0]

            weather_info["sunrise"] = datetime.strptime(weather_info["sunrise"], "%H:%M").astimezone(
                pytz.timezone(weather_info['timezone'])).strftime("%I:%M")
            weather_info["sunset"] = datetime.strptime(weather_info["sunset"], "%H:%M").astimezone(
                pytz.timezone(weather_info['timezone'])).strftime("%I:%M")
            weather_info["ts"] = datetime.fromtimestamp(weather_info["ts"]).strftime("%m-%d-%Y, %H:%M")

            cache.set(f"{city}-weather", weather_info)
        except:
            weather_info = {}
    

    dining_info = cache.get(f"{city}-dinning")
    if not dining_info:
        dining_info = FourSquarePlacesHelper().get_places(
            city=f"{city}, {country}", categories="13065", sort="RELEVANCE", limit=5)
        cache.set(f"{city}-dinning", dining_info)
        
        
    airport_info = cache.get(f"{city}-airport")
    if not airport_info:
        airport_info = FourSquarePlacesHelper().get_places(
            city=f"{city}, {country}", categories="19040", sort="RELEVANCE", limit=5)

        cache.set(f"{city}-airport", airport_info)
        
        
    outdoor_info = cache.get(f"{city}-outdoor")
    if not outdoor_info:
        outdoor_info = FourSquarePlacesHelper().get_places(
            city=f"{city}, {country}", categories="16000", sort="RELEVANCE", limit=5)
        
        cache.set(f"{city}-outdoor", outdoor_info)
    
    
    arts_info = cache.get(f"{city}-arts")
    if not arts_info:
        arts_info = FourSquarePlacesHelper().get_places(
            city=f"{city}, {country}", categories="10000", sort="RELEVANCE", limit=5)
        
        cache.set(f"{city}-arts", arts_info)


    photo_link = cache.get(f"{city}-photolink")
    
    if not photo_link:
        photo_link = UnplashCityPhotoHelper().get_city_photo(city=city)
        cache.set(f"{city}-photolink", photo_link)
        

    print(dining_info)
    return render(
        request, 'search/city_info.html',
        context={
            "weather_info": weather_info,
            "dining_info": dining_info,
            "airport_info": airport_info,
            "outdoor_info": outdoor_info,
            "arts_info": arts_info,
            "photo_link": photo_link,
        }
    )
