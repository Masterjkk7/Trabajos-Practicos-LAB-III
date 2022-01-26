from django.db import models
from django.db.models.fields import IntegerField
from django.utils.html import format_html


# Create your models here.

class Tipo(models.Model):
    nombre = models.CharField(max_length=40) 

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'

class Pokemon(models.Model):
    nombre = models.CharField(max_length=40)
    habilidad = models.CharField(max_length=40)
    tipo = models.ManyToManyField(Tipo, verbose_name='Tipos', related_name='mis_pokemones')
    numero = models.IntegerField()   
    apariencia = models.ImageField(upload_to='sprites/')

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = 'Pokemon'
        verbose_name_plural = 'Pokemones'

    def get_apariencia(self):
        if self.apariencia:
            return format_html("<img style='width:100px'; src='{}'/>".format(self.apariencia.url))
        else:
            return format_html("<img style='width:100px'; src='sprites/default.png'/>")

    get_apariencia.short_description = "Imagen"

class Batalla(models.Model):
    luchadores = models.ManyToManyField(Pokemon)
    fecha = models.DateField(null=True)

    """def __str__(self) -> str:
        return self.luchadores.nombre"""

    class Meta:
        verbose_name = 'Batalla'
        verbose_name_plural = 'Batallas'