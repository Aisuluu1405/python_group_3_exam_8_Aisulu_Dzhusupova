from django.conf import settings
from django.db import models


CATEGORY_CHOICES = (
    ('other', 'Другое'),
    ('individuals', 'Физические лица'),
    ('legal entities', 'Юридические лица'),
    ('сard service', 'Карточное обслуживание'),
    ('internet banking', 'Интернет банкинг'),
)


class Services(models.Model):
    name = models.CharField(max_length=200, verbose_name='Услуги')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0][0],
                                verbose_name='Категория')
    photo = models.ImageField(upload_to='product_images', null=True, blank=True, verbose_name='Фото')
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'



