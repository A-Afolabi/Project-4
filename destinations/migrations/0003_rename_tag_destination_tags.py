# Generated by Django 4.0.3 on 2022-03-07 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0002_destination_continent_destination_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destination',
            old_name='tag',
            new_name='tags',
        ),
    ]