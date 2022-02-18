# Generated by Django 4.0.2 on 2022-02-18 21:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagepost',
            name='slug',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='imagepost',
            name='title',
            field=models.CharField(help_text='Short Title', max_length=25, unique=True),
        ),
        migrations.CreateModel(
            name='ImageGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('gallery', models.ManyToManyField(to='galeria.ImagePost')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
