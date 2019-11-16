# Generated by Django 2.2 on 2019-11-16 12:42

from django.db import migrations

def create_profiles(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Profile = apps.get_model('accounts', 'Profile')
    for user in User.objects.all():
        Profile.objects.get_or_create(user=user)

def drop_profiles(apps, schema_editor):
    Profile = apps.get_model('accounts', 'Profile')
    Profile.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_profile_email'),
    ]

    operations = [
        migrations.RunPython(create_profiles, drop_profiles),
    ]
