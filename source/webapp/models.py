from django.conf import settings
from django.contrib.auth.models import User
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


REVIEW_CHOICES = (
    ('excellent', '5'),
    ('good', '4'),
    ('so-so', '3'),
    ('bad', '2'),
    ('awfully', '1')
)


class Review(models.Model):
    author = models.ForeignKey(User, related_name='user_review', on_delete=models.PROTECT, verbose_name='Автор')
    service = models.ForeignKey('webapp.Services', related_name='service_review', on_delete=models.PROTECT,
                                    verbose_name='Услуга')
    text = models.TextField(max_length=1000, verbose_name='Текст отзыва')
    rating = models.IntegerField(choices=REVIEW_CHOICES, verbose_name='Оценка')

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

