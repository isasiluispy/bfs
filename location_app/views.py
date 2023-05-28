from django.shortcuts import render, redirect
from .models import Location

# import settings
from django.conf import settings


def home(request):
    return render(request, "location_app/home.html")


def location_list(request):
    locations = Location.objects.all()
    return render(
        request,
        "location_app/location_list.html",
        {
            "locations": locations,
            "google_maps_api_key": settings.GOOGLE_MAPS_API_KEY,
        },
    )
