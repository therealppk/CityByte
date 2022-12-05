from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from search.helpers.autocomplete import GenericDBSearchAutoCompleteHelper
from search.helpers.photo import UnplashCityPhotoHelper
from search.utils.search import AmadeusCitySearch
from search.utils.url import URL
from django.contrib.auth.decorators import login_required


@login_required
@require_http_methods(["GET"])
def main_page(request):
    return render(request, "search/search.html", context={"request": request})


@require_http_methods(["GET"])
def city_suggestions(request):
    suggestions_data = GenericDBSearchAutoCompleteHelper(
        klass=AmadeusCitySearch, url=URL(**settings.AMADEUS_CONFIG)
    ).get_suggestions(city=request.GET.get("q"), max=10)

    return JsonResponse({"results": suggestions_data.get("data", [])})


@require_http_methods(["GET"])
def city_photo(request):
    photo_link = UnplashCityPhotoHelper().get_city_photo(
        city=request.GET.get("q")
    )
    return JsonResponse(
        {
            "path": photo_link,
        }
    )
