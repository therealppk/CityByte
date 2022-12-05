from django.test import SimpleTestCase
from django.urls import reverse, resolve
from info.views import profile_page


class TestUrls(SimpleTestCase):
    def test_profile_page(self):
        url = reverse("profile_page")
        self.assertEquals(resolve(url).func, profile_page)
