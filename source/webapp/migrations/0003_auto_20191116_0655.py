# Generated by Django 2.2 on 2019-11-16 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(5, 'excellent'), (4, 'good'), (3, 'so-so'), (2, 'bad'), (1, 'awfully')], verbose_name='Оценка'),
        ),
    ]
