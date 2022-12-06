from datetime import datetime
import json
import pytz
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from info.helpers.places import FourSquarePlacesHelper
from info.helpers.weather import WeatherBitHelper
from search.helpers.photo import UnplashCityPhotoHelper
from .models import CitySearchRecord, Comment, FavCityEntry
from django.core.cache import cache
from .forms import CommentForm

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count


@login_required()
def addTofav(request):

    city = request.GET.get("city")
    country = request.GET.get("country")

    if not city or not country:
        return JsonResponse({"data": None})

    data = "removed"

    # if count is 0 add to list else remove
    count = FavCityEntry.objects.filter(
        city=city, country=country, user=request.user
    ).count()

    if count > 0:
        FavCityEntry.objects.filter(
            city=city, country=country, user=request.user
        ).delete()

    else:
        FavCityEntry.objects.create(
            city=city, country=country, user=request.user
        )

        data = "added"

    return JsonResponse({"data": data})


@require_http_methods(["GET"])
def place_photo(request):
    photo_link = cache.get(f"photo-link-{request.GET.get('fsq_id')}")

    if not photo_link:
        photo_link = FourSquarePlacesHelper().get_place_photo(
            fsq_id=request.GET.get("fsq_id")
        )
        cache.set(f"photo-link-{request.GET.get('fsq_id')}", photo_link)
    return redirect(photo_link)


@require_http_methods(["GET", "POST"])
def info_page(request):
    city = request.GET.get("city")
    country = request.GET.get("country")

    if request.method == "POST":
        commentForm = CommentForm(request.POST)

        if commentForm.is_valid():
            # save the form data to model
            form = commentForm.save(commit=False)
            form.author = request.user
            form.city = city
            form.country = country
            print(form)
            form.save()

    commentForm = CommentForm()

    # if (
    #     CitySearchRecord.objects.filter(city_name=city, country_name=country).count()
    #     == 0
    # ):
    CitySearchRecord.objects.create(city_name=city, country_name=country)

    # try cache first
    weather_info = cache.get(f"{city}-weather")
    if not weather_info:
        try:
            weather_info = WeatherBitHelper().get_city_weather(
                city=city, country=country
            )["data"][0]

            weather_info["sunrise"] = (
                datetime.strptime(weather_info["sunrise"], "%H:%M")
                .astimezone(pytz.timezone(weather_info["timezone"]))
                .strftime("%I:%M")
            )
            weather_info["sunset"] = (
                datetime.strptime(weather_info["sunset"], "%H:%M")
                .astimezone(pytz.timezone(weather_info["timezone"]))
                .strftime("%I:%M")
            )
            weather_info["ts"] = datetime.fromtimestamp(
                weather_info["ts"]
            ).strftime("%m-%d-%Y, %H:%M")

            cache.set(f"{city}-weather", weather_info)
        except Exception:
            weather_info = {}

    dining_info = cache.get(f"{city}-dinning")
    if not dining_info:
        dining_info = FourSquarePlacesHelper().get_places(
            city=f"{city}, {country}",
            categories="13065",
            sort="RELEVANCE",
            limit=5,
        )
        cache.set(f"{city}-dinning", dining_info)

    airport_info = cache.get(f"{city}-airport")
    if not airport_info:
        airport_info = FourSquarePlacesHelper().get_places(
            city=f"{city}, {country}",
            categories="19040",
            sort="RELEVANCE",
            limit=5,
        )

        cache.set(f"{city}-airport", airport_info)

    outdoor_info = cache.get(f"{city}-outdoor")
    if not outdoor_info:
        outdoor_info = FourSquarePlacesHelper().get_places(
            city=f"{city}, {country}",
            categories="16000",
            sort="RELEVANCE",
            limit=5,
        )

        cache.set(f"{city}-outdoor", outdoor_info)

    arts_info = cache.get(f"{city}-arts")
    if not arts_info:
        arts_info = FourSquarePlacesHelper().get_places(
            city=f"{city}, {country}",
            categories="10000",
            sort="RELEVANCE",
            limit=5,
        )

        cache.set(f"{city}-arts", arts_info)

    photo_link = cache.get(f"{city}-photolink")
    if not photo_link:
        photo_link = UnplashCityPhotoHelper().get_city_photo(city=city)
        cache.set(f"{city}-photolink", photo_link)

    comments = Comment.objects.filter(city=city, country=country).order_by(
        "-created_on"
    )
    isInFav = (
        True
        if FavCityEntry.objects.filter(
            city=city, country=country, user=request.user
        ).count()
        > 0
        else False
    )
    return render(
        request,
        "search/city_info.html",
        context={
            "weather_info": weather_info,
            "dining_info": dining_info,
            "airport_info": airport_info,
            "outdoor_info": outdoor_info,
            "arts_info": arts_info,
            "photo_link": photo_link,
            "comments": comments,
            "commentForm": commentForm,
            "city": city,
            "country": country,
            "isInFav": isInFav,
        },
    )


@login_required()
def profile_page(request):

    favCities = FavCityEntry.objects.filter(user=request.user)
    popularCities = (
        CitySearchRecord.objects.values("city_name")
        .annotate(city_count=Count("city_name"))
        .order_by("-city_count")[:10]
    )

    return render(
        request,
        "profile/profile.html",
        {"favCities": favCities, "popularCities": popularCities},
    )
