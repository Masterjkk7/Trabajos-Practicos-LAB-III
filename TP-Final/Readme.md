﻿<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/International_Pok%C3%A9mon_logo.svg/2560px-International_Pok%C3%A9mon_logo.svg.png" alt="Sublime's custom image"/>
</p>

# POKEPEDIA

## ¿En qué consiste?

Nuestro proyecto cuenta con un sitio le permite al usuario buscar un pokemon, ya sea por su nombre o su número, y que como resultado obtenga los datos principales del pokemon en cuestión, esto se realiza mediante el uso de una **API** que se encarga de traer la información requerida para que luego sea administrada a través de nuestro código.

Los datos que se consideran son:

* Nombre

* Número

* Tipo

* Habilidad

* Apariencia

## Como está hecho

El programa funciona utilizando **Django** por lo que se maneja principalmente con **Python** y empleamos **Bootstrap** para nuestros archivos **HTML**.

## Uso del sitio

Una vez se encuentre en marcha la aplicación de Django y este abierto el sitio, se debe escribir el **nombre o número** del pokemon en la barra de búsqueda que se encuentra en la parte superior derecha de la página, luego se debe apretar el botón que dice **Buscar**:

* Si la búsqueda fue exitosa se mostrará un cuadro con la imagen del pokemon y todos sus datos.

* Si no fue exitosa se mostrará un mensaje de error que indicará esto mismo y se refrescará la página.

Si en vez de buscar un pokemon se quiere registrar uno propio el usuario puede apretar la palabra **Admin** que se encuentra en la parte superior izquierda de la página para administrar todos los registros y poder guardar su propia creación.
