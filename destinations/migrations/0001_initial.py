# Generated by Django 4.0.3 on 2022-03-03 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50)),
                ('price', models.PositiveIntegerField(default=None)),
                ('duration', models.PositiveIntegerField(default=None)),
                ('ability_level', models.CharField(default=None, max_length=20)),
                ('image', models.CharField(default=None, max_length=500)),
                ('background_image', models.CharField(default=None, max_length=500)),
                ('description', models.CharField(default=None, max_length=500)),
            ],
        ),
    ]
