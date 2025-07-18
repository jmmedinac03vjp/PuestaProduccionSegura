Actividad 3 - Unidad 0
Uso de Git
===============
Tenemos los siguientes documentos:
1.
Actividad 3 - Unidad 0. Uso de Git
===
Vamos a trabajar con Git.

El producto a realizar será la creación un repositorio (con nombre PPSActividad3Unidad0TuNombre) en la [plataforma de GitHub](https://github.com/)  que contenga un conjunto de archivos donde tendremos archivos de documentación de todo el proceso realizado (en formato .md) junto con el resto de archivos necesarios, imágenes, etc...

Para realizar la actividad te sugiero que sigas el documento de Victor Ponz que se encuentra en la sección de recursos. Con él vamos a poder aprender qué es Git, cómo se instala y cómo se trabaja. 

# INDICE

[Pasos a Realizar](#pasos-a-seguir)

[Contenidos del repositorio](#Contenidos-del-repositorio)

[Primeros Pasos](#Primeros-pasos)

[Uso de git](uso.md)

[Creación de Contenedor GitLab](#Creación-de-Contenedor-GitLab)

# Pasos a seguir

Los pasos a realizar son los siguientes

1. Abre una cuenta en Github.com con tu cuenta de @informatica.iesvalledeljerteplasencia.es.

2. Instala git y php en tu equipo.

3. Configura tu cuenta y git correctamente.
> - Recuerda que tienes que crear una clave y añadirla en git [puedes consultar 
éste artículo](https://juncotic.com/repositorios-git-ssh/) 


>### Contenidos del repositorio
 
 El repositorio deberá de contener al menos los siguientes archivos y carpetas:

+ Carpeta "Images" con las imágenes y capturas que aparecen el los ficheros.md
+ README.md donde se incluirá una introducción.
  - Tendrá enlaces al resto de los archivos .md del repositorio.
+ Install.md donde se explicará el proceso de instalación y configuración de Git en nuestro equipo local.
  - Habrá dos secciones:Instalación y configuración. Habrá enlaces interno para ir a cada una de las secciones.
  - Aquí deberás de incluir ``fragmentos de código`` en vez de captura de pantalla. Bien incrustados o 
~~~
     /// codigo en 
     /// varias líneas
~~~

+ UsoGit.md donde indicaremos los comandos principales que usamos en Git.
+ GitHub.md donde explicaremos el proceso de apertura de cuenta, login y funcionamiento básico de la plataforma github.com (deberemos de crear cuenta o utilizar una asociada al correo del centro).
+ GitLab.md donde explicaremos el proceso para levantar un contenedor docker en nuestra máquina con una instancia de GitLab.

> ### Primeros pasos
1. Crea un nuevo repositorio en gitHub y lo clonas en tu equipo. El repositorio debe de llevar por nombre PPS0-Unidad0Actividad3-1TuNombre. ``git init``)
6. Crea los archivos y directorios necesarios y los añades al proyecto.Haz un listado en forma de arbol (tree -a) de todos los archivos del directorio.
2. Comprueba el estado ``git status``
3. Añade los diferentes archivos y carpetas ``git add ``o ``git add -A``
4. Modifica algún archivo y vuelves a comprobar su estado.
5. Haz un ``commit``como comentario indica que es la creación de archivos y vuelves a comprobar su estado
6. Sube los cambios al repositorio remoto ``git push origin main` y comprueba si todo se visualiza correctamente 



Una vez que tengas todo preparado 
En github.com busca y clona el proyecto de victorponz/Ciberseguridad-PePS
Crea un archivo con nombre index.php. Introduce el código html para que nos muestre un mensaje de Hola mundo con tu nombre.
Añade el archivo index.php al proyecto.
Ejecuta php -S 0:8080 para lanzar un servidor con la página html que has creado.
Puedes acceder a ella en http://localhost:8080
Modifica el fichero index.php
Verifica estado del proyecto.
Refresca navegador para comprobar que ha cambiado.
Vuelve a la versión anterior del archivo index.php (git restore).
Vuelve a refrescar navegador para ver como vuelve a versión inicial.
Para finalizar y ver cómo funcionan los comandos pull y push, haz un push y comprueba cómo han subido los archivos a github.com.
Modifica el archivo index.php desde la página de github.com y haz un pull y comprueba cómo se ha modificado la página web en nuestro navegador.
Vamos ahora una pequeña aplicación que nos va a permitir ver información y avatar subida por nosotros: 


Clona el repositorio https://github.com/jmmedinac03vjp/pps0-1
Visualiza con php el contenido de la página web.
Introduce dentro de la carpeta img una imagen de tu avatar.
Dentro de la carpeta profile crea un archivo html con el mismo nombre del archivo de la imagen que copiaste.
Lanza el comando php para que se muestre el contenido de la página web y ver cómo se ha modificado.
Visualiza el estado del proyecto  (git status)


## Creación-de-Contenedor-GitLab
Entrega un documento explicando estos los pasos principales y resultados, no es necesario que adjuntes capturas de pantalla de cada uno de los puntos ni del proceso de instalación.

Esta actividad se relaciona con el resultado de aprendizaje RA5b
