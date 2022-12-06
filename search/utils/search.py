from abc import ABC, abstractmethod

import requests
from django.conf import settings

from search.utils.url import URL


class SearchUtilBase(ABC):
    _url: URL = None

    def __init__(self, url: URL):
        self._url = url

    @abstractmethod
    def get_city_suggestions(self, city: str, **kwargs):
        pass


class GeoDB(SearchUtilBase):
    def get_city_suggestions(self, city: str, **kwargs):
        offset = kwargs.get("offset", 0)
        limit = kwargs.get("limit", 10)

        response = requests.request(
            "GET",
            str(self._url.get_url(path="/v1/geo/cities")),
            headers=self._url.with_default_headers(),
            params=self._url.with_default_headers(
                {"namePrefix": city, "offset": offset, "limit": limit}
            ),
        )

        return response.json()


class AmadeusCitySearch(SearchUtilBase):
    def __init__(self, url: URL):
        self._access_token = None
        super().__init__(url)

    def get_city_suggestions(self, city: str, **kwargs):
        params = self._url.with_default_params({"keyword": city})
        params.update(kwargs)

        success = False

        while not success:
            response = requests.request(
                "GET",
                str(
                    self._url.get_url(
                        path="/v1/reference-data/locations/cities"
                    )
                ),
                headers={"Authorization": f"Bearer {self._access_token}"},
                params=params,
            )

            if (
                response.json().get("errors")
                and response.json()["errors"][0]["status"] == 401
            ):
                response = requests.request(
                    "POST",
                    str(self._url.get_url(path="/v1/security/oauth2/token")),
                    headers={
                        "Content-Type": "application/x-www-form-urlencoded"
                    },
                    data={
                        "grant_type": "client_credentials",
                        "client_id": settings.AMADEUS_CONFIG["headers"][
                            "API_KEY"
                        ],
                        "client_secret": settings.AMADEUS_CONFIG["headers"][
                            "API_SECRET_KEY"
                        ],
                    },
                )

                self._access_token = response.json()["access_token"]
            else:
                success = True

        return response.json()
