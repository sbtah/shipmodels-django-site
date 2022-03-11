# Generated by Django 4.0.2 on 2022-03-11 18:01

from django.db import migrations, models
import functools
import gallery.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytuł', models.CharField(max_length=50, unique=True, verbose_name='Tytuł')),
                ('slug', models.CharField(blank=True, help_text='Automatycznie generowany', max_length=100, null=True, unique=True, verbose_name='Link')),
                ('opis_modelu', models.TextField(blank=True, null=True, verbose_name='Opis modelu')),
                ('skala_modelu', models.CharField(blank=True, max_length=50, null=True, verbose_name='Skala modelu')),
                ('długość_modelu', models.CharField(blank=True, max_length=50, null=True, verbose_name='Długość modelu')),
                ('szerokość_modelu', models.CharField(blank=True, max_length=50, null=True, verbose_name='Szerokość modelu')),
                ('wysokość_modelu', models.CharField(blank=True, max_length=50, null=True, verbose_name='Wysokość modelu')),
                ('waga_modelu', models.CharField(blank=True, max_length=50, null=True, verbose_name='Waga modelu')),
                ('dodano', models.DateTimeField(auto_now_add=True, verbose_name='Dodano')),
                ('zaktualizowano', models.DateTimeField(auto_now=True, verbose_name='Zaktualizowano')),
            ],
            options={
                'verbose_name_plural': 'Galleries',
                'ordering': ('-dodano',),
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytuł', models.CharField(help_text='Krótki tytuł', max_length=50, unique=True, verbose_name='Tytuł')),
                ('slug', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Link')),
                ('obraz', models.ImageField(blank=True, default='images/default.jpg', null=True, upload_to=functools.partial(gallery.utils._update_filename, *(), **{'path': 'images/'}), verbose_name='Obraz')),
                ('obraz_opis', models.CharField(help_text='Alt opis dla zdjęcia', max_length=100, verbose_name='Obraz SEO opis')),
                ('dodano', models.DateTimeField(auto_now_add=True, verbose_name='Dodano')),
                ('zaktualizowano', models.DateTimeField(auto_now=True, verbose_name='Zaktualizowano')),
                ('użyty', models.BooleanField(default=False, verbose_name='Użyty')),
                ('użyty_w_galerii', models.CharField(blank=True, max_length=100, null=True, verbose_name='Użyty w galerii:')),
            ],
            options={
                'ordering': ('-dodano',),
            },
        ),
    ]
