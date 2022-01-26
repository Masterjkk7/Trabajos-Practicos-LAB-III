# Generated by Django 4.0.1 on 2022-01-26 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokepedia', '0005_batalla_ganador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('foto', models.ImageField(upload_to='lugares/')),
            ],
            options={
                'verbose_name': 'Lugar',
                'verbose_name_plural': 'Lugares',
            },
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='tipo',
            field=models.ManyToManyField(related_name='mis_pokemones', to='pokepedia.Tipo'),
        ),
    ]