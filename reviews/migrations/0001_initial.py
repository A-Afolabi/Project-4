# Generated by Django 4.0.3 on 2022-03-04 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(default=None, max_length=160)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
