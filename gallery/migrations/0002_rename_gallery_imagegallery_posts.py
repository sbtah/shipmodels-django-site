# Generated by Django 4.0.2 on 2022-03-03 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagegallery',
            old_name='gallery',
            new_name='posts',
        ),
    ]