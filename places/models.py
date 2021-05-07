from django.db import models
from tinymce import models as tinymce_models


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Сокращенное описание', blank=True)
    description_long = tinymce_models.HTMLField('Полное описание', blank=True)
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def get_place_description(self):
        place_images = self.images.all().order_by('number')
        images_url = [place_image.image.url for place_image in place_images]
        return {
            'title': self.title,
            'imgs': images_url,
            'description_short': self.description_short,
            'description_long': self.description_long,
            'coordinates': {
                'lng': self.lon,
                'lat': self.lat,
            },
        }


class Image(models.Model):
    number = models.IntegerField('Номер картинки')
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='Место, которому принадлежит фото',
        related_name='images',
    )
    image = models.ImageField('Изображение')

    def __str__(self):
        return f'{self.number} {self.place.title}'

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
        ordering = ['number']
