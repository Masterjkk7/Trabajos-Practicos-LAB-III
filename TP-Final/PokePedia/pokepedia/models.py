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
    tipo = models.ManyToManyField(Tipo)
    numero = models.IntegerField()   
    apariencia = models.ImageField(upload_to='sprites/')

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = 'Pokemon'
        verbose_name_plural = 'Pokemones'

    def get_apariencia(self):
        if self.apariencia:
            return format_html("<img style='width:150px'; src='{}'/>".format(self.apariencia.url))
        else:
            return format_html("<img style='width:150px'; src='/media/sprites/default.png'/>")

    get_apariencia.short_description = "Imagen"

class Lugar(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='lugares/')

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = 'Lugar'
        verbose_name_plural = 'Lugares'

    def get_foto(self):
        if self.foto:
            return format_html("<img style='width:150px'; src='{}'/>".format(self.foto.url))
        else:
            return format_html("<img style='width:150px'; src='foto/default.png'/>")

    get_foto.short_description = "Foto"


class Batalla(models.Model):
    luchadores = models.ManyToManyField(Pokemon)
    ganador = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='ganador', null=True)
    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE, null=True)
    fecha = models.DateField(null=True)

    def __str__(self) -> str:
        return str(self.fecha)

    class Meta:
        verbose_name = 'Batalla'
        verbose_name_plural = 'Batallas'