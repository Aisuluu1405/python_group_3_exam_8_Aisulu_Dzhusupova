# Generated by Django 2.2 on 2019-11-16 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20191116_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_review', to='webapp.Services', verbose_name='Услуга'),
        ),
    ]