# Generated by Django 4.0.1 on 2022-01-25 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokepedia', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batalla',
            name='duracion',
        ),
    ]
