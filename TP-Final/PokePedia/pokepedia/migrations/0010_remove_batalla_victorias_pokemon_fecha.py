# Generated by Django 4.0.1 on 2022-02-21 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokepedia', '0009_remove_pokemon_victorias_batalla_victorias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batalla',
            name='victorias',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='fecha',
            field=models.DateField(null=True),
        ),
    ]
