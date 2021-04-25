from django.db import models


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Сокращенное описание', blank=True)
    description_long = models.TextField('Полное описание', blank=True)
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class Image(models.Model):
    number = models.IntegerField('Номер картинки')
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='Место, которому принадлежит фото',
        related_name='places'
    )
    image = models.ImageField('Изображение')

    def __str__(self):
        return f'{self.number} {self.place.title}'

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
