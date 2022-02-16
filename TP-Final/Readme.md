<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/International_Pok%C3%A9mon_logo.svg/2560px-International_Pok%C3%A9mon_logo.svg.png" alt="Sublime's custom image"/>
</p>


<![endif]-->

# POKEPEDIA

## ¿En qué consiste?

Nuestro proyecto cuenta con un sitio le permite al usuario buscar un pokemon, ya sea por su nombre o su número, y que como resultado obtenga los datos principales del pokemon en cuestión, esto se realiza mediante el uso de una **API** que se encarga de traer la información requerida para que luego sea administrada a través de nuestro código, dicha información es almacenada en una base datos para que su acceso en el futuro sea más rápido.

Los datos que se consideran son:

* Nombre

* Número

* Tipo

* Habilidad

* Apariencia

Además, dentro de **Admin** podemos gestionar completamente los registros realizados en la base de datos y esto nos permite utilizar las otras funcionalidades del proyecto:

* Registrar Tipos y Pokemones **propios**.

* Registrar **Lugares** que luego serán usados para registrar **Batallas** (Una batalla consiste en un evento que ya ocurrió en una determinada fecha y lugar, del cual participaron Pokemones y uno salió ganador).

## Infraestructura

El programa funciona utilizando **Django** como base, por lo que se maneja principalmente con el lenguaje **Python** para el **Back-End** y en cuanto al **Front-End** empleamos las librerías **Bootstrap** y **JQuery** para nuestro **HTML**.

### PokeApi

Este es el nombre de la [API](https://pokeapi.co/) que decidimos implementar, es completamente **gratis** y su uso es **libre**, también cabe aclarar que al tratarse de una API orientada únicamente al consumo solo admite el método **HTTP GET**. El objetivo de sus creadores es centralizar toda la información posible sobre los Pokemon en un solo lugar, esto implica que la cantidad de información que maneja es abismal por lo que nosotros utilizamos únicamente un **endpoint** que provee todo lo que necesitamos para nuestro sitio: https://pokeapi.co/api/v2/pokemon/.

### Django-Admin-Interface

Se trata de una [interfaz](https://github.com/fabiocaccamo/django-admin-interface) que incluimos en nuestro proyecto que nos permite customizar la apariencia del Admin de Django.

## Instalación

1. Descargar el repositorio.

2. Instalar virtualenvwrapper, esto se puede realizar abriendo una consola y ejecutando el comando: `pip install virtualenvwrapper`.

3. Crear un entorno virtual utilizando el comando: `mkvirtualenv "nombre del entorno"`.

4. Abrir el entorno virtual creado con: `workon "nombre del entorno"`.

5. Moverse dentro de la consola hacia la carpeta "TP-Final", esto se puede hacer con el comando: `cd "ruta de la carpeta"`.

6. Instalar requirements.txt dentro del entorno: `pip install requirements.txt`.

7. Moverse a la carpeta "PokePedia": `cd PokePedia`.

8. Ingresar los siguientes comandos: `python manage.py makemigrations` y `pyton manage.py migrate`.

9. Poner en marcha el servidor con: `python manage.py runserver`.

## Uso del sitio

Una vez se encuentre en marcha la aplicación de Django y este abierto el sitio, se debe escribir el **nombre o número** del pokemon en la barra de búsqueda que se encuentra en la parte superior derecha de la página, luego se debe apretar el botón que dice **Buscar**:

* Si la búsqueda fue exitosa se mostrará un cuadro con la imagen del pokemon y todos sus datos.

* Si no fue exitosa se mostrará un mensaje de que permitirá buscarlo en la API, si es encontrado se mostrara y si no se indicara que no se obtuvieron resultados.

Si en vez de buscar un pokemon se quiere gestionar los ya registrados o utilizar las otras funciones del sitio se puede presionar la palabra **Admin** que se encuentra en la parte superior izquierda, aquí se pueden registrar tanto Tipos y Pokemon propios como Lugares y Batallas.
