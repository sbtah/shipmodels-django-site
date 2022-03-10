# Generated by Django 4.0.2 on 2022-03-10 21:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gallery', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='dodał',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Dodał'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='główne_zdjęcie',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='main_image', to='gallery.image', verbose_name='Główne zdjęcie'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='zdjęcia',
            field=models.ManyToManyField(to='gallery.Image', verbose_name='Zdjęcia'),
        ),
    ]
