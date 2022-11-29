from datetime import datetime

import pytz
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from info.helpers.places import FourSquarePlacesHelper
from info.helpers.weather import WeatherBitHelper
from search.helpers.photo import UnplashCityPhotoHelper


@require_http_methods(["GET"])
def place_photo(request):
    photo_link = FourSquarePlacesHelper().get_place_photo(fsq_id=request.GET.get('fsq_id'))
    return redirect(photo_link)


@require_http_methods(["GET"])
def info_page(request):
    city = request.GET.get("city")
    country = request.GET.get("country")
    
    try:

        weather_info = WeatherBitHelper().get_city_weather(city=city, country=country)["data"][0]

        weather_info["sunrise"] = datetime.strptime(weather_info["sunrise"], "%H:%M").astimezone(
            pytz.timezone(weather_info['timezone'])).strftime("%I:%M")
        weather_info["sunset"] = datetime.strptime(weather_info["sunset"], "%H:%M").astimezone(
            pytz.timezone(weather_info['timezone'])).strftime("%I:%M")
        weather_info["ts"] = datetime.fromtimestamp(weather_info["ts"]).strftime("%m-%d-%Y, %H:%M")

    except:
        weather_info = {}
    
    dining_info = FourSquarePlacesHelper().get_places(
        city=f"{city}, {country}", categories="13065", sort="RELEVANCE", limit=5)
    airport_info = FourSquarePlacesHelper().get_places(
        city=f"{city}, {country}", categories="19040", sort="RELEVANCE", limit=5)
    outdoor_info = FourSquarePlacesHelper().get_places(
        city=f"{city}, {country}", categories="16000", sort="RELEVANCE", limit=5)
    arts_info = FourSquarePlacesHelper().get_places(
        city=f"{city}, {country}", categories="10000", sort="RELEVANCE", limit=5)

    photo_link = UnplashCityPhotoHelper().get_city_photo(city=city)

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
