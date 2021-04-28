import os

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

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
                "placeId": place.id,
                "detailsUrl": os.path.join(STATIC_URL, 'places/moscow_legends.json')
            }
        }
        features.append(place_feature)

    places_features = {
        "type": "FeatureCollection",
        "features": features
    }

    return render(request, 'index.html', context={'places': places_features})


def get_place_by_id(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place_images = place.images.all()
    images_url = [place_image.image.url for place_image in place_images]
    place_feature = {
        'title': place.title,
        'imgs': images_url,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.lon,
            'lat': place.lat
        },
    }
    response = JsonResponse(
        place_feature,
        safe=False,
        json_dumps_params={'ensure_ascii': False, 'indent': 2}
    )
    return response
