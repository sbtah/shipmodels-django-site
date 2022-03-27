# Generated by Django 4.0.2 on 2022-03-27 10:09

import banners.models
from django.db import migrations, models
import functools
import gallery.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannerImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytuł', models.CharField(help_text='Tytuł', max_length=50)),
                ('obraz', models.ImageField(blank=True, default='banners/default.jpg', null=True, upload_to=functools.partial(gallery.utils._update_filename, *(), **{'path': 'banners/'}), verbose_name='Obraz baneru')),
                ('obraz_opis', models.CharField(help_text='Alt opis dla zdjęcia', max_length=100, verbose_name='Obraz SEO opis')),
            ],
        ),
        migrations.CreateModel(
            name='AboutBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytuł', models.CharField(max_length=50, unique=True, verbose_name='Tytuł')),
                ('is_active', models.BooleanField(default=False, validators=[banners.models.validate_active_status], verbose_name='Aktywny')),
                ('zdjęcia', models.ManyToManyField(to='banners.BannerImage', verbose_name='Zdjęcia')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
