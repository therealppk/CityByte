from abc import ABC, abstractmethod

import requests

from search.utils.url import URL


class PhotoUtilBase(ABC):
    _url: URL = None

    def __init__(self, url: URL):
        self._url = url

    @abstractmethod
    def get_photos(self, city: str, **kwargs):
        pass


class Unsplash(PhotoUtilBase):
    class Orientation:
        LANDSCAPE = "landscape"
        PORTRAIT = "portrait"

    def get_photos(self, query: str, **kwargs):
        page = kwargs.get("page", 1)
        orientation = kwargs.get("orientation", Unsplash.Orientation.LANDSCAPE)

        response = requests.request(
            "GET",
            str(self._url.get_url(path="/search/photos")),
            headers=self._url.with_default_headers(),
            params=self._url.with_default_params(
                {"page": page, "orientation": orientation, "query": query}
            ),
        )

        return response.json().get("results", [])
