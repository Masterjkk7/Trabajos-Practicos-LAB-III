# Generated by Django 4.0.1 on 2022-02-21 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokepedia', '0008_pokemon_victorias_alter_batalla_lugar_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='victorias',
        ),
        migrations.AddField(
            model_name='batalla',
            name='victorias',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
