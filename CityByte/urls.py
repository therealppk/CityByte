"""CityByte URL Configuration
 
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
 
from search.views import main_page
from info.views import info_page
 
urlpatterns = [
    path('', main_page, name="main_page"),
    path("accounts/", include("django.contrib.auth.urls")), 
    path('city', info_page, name="info_page"),
    path('admin/', admin.site.urls),
    path('api/search/', include(("search.urls", "search"), namespace="search")),
    path('api/info/', include(("info.urls", "info"), namespace="info")),
]