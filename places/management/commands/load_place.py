from urllib.parse import urlparse

import requests
import urllib3
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandError
from requests import HTTPError

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Loading a location description from a file'

    def add_arguments(self, parser):
        parser.add_argument('file_url', type=str)

    def handle(self, *args, **options):
        urllib3.disable_warnings()
        try:
            response = requests.get(options['file_url'], verify=False)
            response.raise_for_status()
            review_result = response.json()

            place, created_place = Place.objects.get_or_create(
                title=review_result['title'],
                defaults={
                    'lat': review_result['coordinates']['lat'],
                    'lon': review_result['coordinates']['lng'],
                    'description_short': review_result['description_short'],
                    'description_long': review_result['description_long'],
                }
            )

            for number, image_url in enumerate(review_result['imgs'], start=1):
                image, created_image = Image.objects.get_or_create(
                    number=number,
                    place=place,
                )
                response = requests.get(image_url, verify=False)
                response.raise_for_status()
                file_name = urlparse(image_url).path.split('/')[-1]
                image.image.save(file_name, ContentFile(response.content), save=True)

            self.stdout.write(self.style.SUCCESS(f'Загружено описание для {review_result["title"]}, '
                                                 f'добавлено {number} фотографий'))
        except HTTPError:
            raise CommandError('Ошибка загрузки')
