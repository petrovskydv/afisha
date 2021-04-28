import os

from django.shortcuts import render

from places.models import Place
from where_to_go.settings import STATIC_URL


def index(request):
    print("новое приложение")
    places = Place.objects.all()
    features = []
    for place in places:
        place_feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lon, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": "moscow_legends",
                "detailsUrl": os.path.join(STATIC_URL, 'places/moscow_legends.json')
            }
        }
        features.append(place_feature)

    places_features = {
        "type": "FeatureCollection",
        "features": features
    }

    return render(request, 'index.html', context={'places': places_features})
