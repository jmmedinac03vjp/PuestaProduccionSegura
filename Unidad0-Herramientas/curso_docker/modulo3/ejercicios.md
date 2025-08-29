

# Ejercicios

## Ejercicios para repasar

Vamos a trabajar con volúmenes docker:
1. Crea un volumen docker que se llame `miweb`.
2. Crea un contenedor desde la imagen `php:7.4-apache` donde montes en el directorio `/var/www/html` (que sabemos que es el *DocuemntRoot* del servidor que nos ofrece esa imagen) el volumen docker que has creado.
3. Utiliza el comando `docker cp` para copiar un fichero `index.html` en el directorio `/var/www/html`.
4. Accede al contenedor desde el navegador para ver la información ofrecida por el fichero `index.html`.
5. Borra el contenedor
6. Crea un nuevo contenedor y monta el mismo volumen como en el ejercicio anterior.
7. Accede al contenedor desde el navegador para ver la información ofrecida por el fichero `index.html`. ¿Seguía existiendo ese fichero?

Vamos a trabajar con bind mount:
1. Crea un directorio en tu host y dentro crea un fichero `index.html`.
2. Crea un contenedor desde la imagen `php:7.4-apache` donde montes en el directorio `/var/www/html` el directorio que has creado por medio de `bind mount`.
3. Accede al contenedor desde el navegador para ver la información ofrecida por el fichero `index.html`.
4. Modifica el contenido del fichero `index.html` en tu host y comprueba que al refrescar la página ofrecida por el contenedor, el contenido ha cambiado.
5. Borra el contenedor
6. Crea un nuevo contenedor y monta el mismo directorio como en el ejercicio anterior.
7. Accede al contenedor desde el navegador para ver la información ofrecida por el fichero `index.html`. ¿Se sigue viendo el mismo contenido?

## Ejercicios para entregar


### Despliegue de Nextcloud + mariadb/postgreSQL

Vamos a desplegar la aplicación nextcloud con una base de datos (puedes elegir mariadb o PostgreSQL) (**NOTA: Para que no te de errores utiiliza la imagen `mariadb:10.5`**). Te puede servir el ejercicio que hemos realizado para desplegar [Wordpress](wordpress.html). Para ello sigue los siguientes pasos:

1. Crea una red de tipo bridge.
2. Crea el contenedor de la base de datos conectado a la red que has creado. La base de datos se debe configurar para crear una base de dato y un usuario. Además el contenedor debe utilizar almacenamiento (volúmenes o bind mount) para guardar la información. Puedes seguir la documentación de [mariadb](https://hub.docker.com/_/mariadb) o la de [PostgreSQL](https://hub.docker.com/_/postgres).
3. A continuación, siguiendo la documentación de la imagen [nextcloud](https://hub.docker.com/_/nextcloud), crea un contenedor conectado a la misma red, e indica las variables adecuadas para que se configure de forma adecuada y realice la conexión a la base de datos. El contenedor también debe ser persistente usando almacenamiento.
4. Accede a la aplicación usando un navegador web.

Deberás entregar los siguientes pantallazos comprimidos en un zip o en un documento pdf:

* Pantallazo con la instrucción para crear el contenedor de la base de datos.
* Pantallazo con la instrucción para crear el contenedor de la aplicación.
* Pantallazo donde se ve el acceso a la aplicación desde un navegador web.
### Creación y uso de volúmenes

1. Crear los siguientes volúmenes con la orden `docker volume`: *volumen_datos* y *volumen_web*.
2. Una vez creados estos contenedores:
    * Arrancar un contenedor llamado `c1` sobre la imagen `php:7.4-apache` que monte el volumen_web en la ruta `/var/www/html` y que sea accesible en el puerto 8080.
    * Arrancar un contenedor llamado `c2` sobre la imagen `mariadb` que monte el volumen_datos en la ruta `/var/lib/mysql` y cuya contraseña de `root` sea `admin`.

3. Intenta borrar el volumen *volumen_datos*, para ello tendrás  que parar y borrar el contenedor `c2` y tras ello borrar el volumen.
4. Copia o crea un fichero `index.html` al contenedor `c1`, accede al contenedor y comprueba que se está visualizando.
5. Borra el contenedor `c1` y crea un contenedor `c3` con las mismas características que `c1` pero sirviendo en el puerto 8081.

Deberás entregar los siguientes pantallazos comprimidos en un zip o en un documento pdf:

* Pantallazo donde se puedan ver los dos volúmenes creados.
* Pantallazo con la orden correspondiente para arrancar el contenedor c1 usando el *volumen_web*.
* Pantallazo con la orden correspondiente para arrancar el contenedor c2 usando el *volumen_datos*.
* Pantallazo donde se vea el proceso para poder borrar el *volumen_datos*.
* Pantallazo donde se vea el borrado de `c1` y la creación de `c3`.
* Pantallazo donde se vea el acceso al contenedor `c3`.

### Bind mount para compartir datos

1. Crea una carpeta llamada `saludo` y dentro de ella crea un fichero llamado `index.html` con el siguiente contenido (Deberás sustituir ese XXXXXx por tu nombre.):

    ```html
    <h1>HOLA SOY XXXXXX</h1>
    ```    
2. Una vez hecho esto arrancar dos contenedores basados en la imagen php:7.4-apache que hagan un bind mount de la carpeta `saludo` en la carpeta `/var/www/html` del contenedor. Uno de ellos vamos a acceder con el puerto 8181 y el otro con el 8282. Y su nombres serán `c1` y `c2`. 
3. Modifica el contenido del fichero `~/saludo/index.html`.
4. Comprueba que puedes seguir accediendo a los contenedores, sin necesidad de reiniciarlos.

Deberás entregar los siguientes pantallazos comprimidos en un zip o en un documento pdf:

* Pantallazo con la orden correspondiente para arrancar el contenedor c1 (puerto 8181) realizando el bind mount solicitado. 
* Pantallazo con la orden correspondiente para arrancar el contenedor c2 (puerto 8282) realizando el bind mount solicitado. 
* Pantallazo donde se pueda apreciar que accediendo a `c1` se puede ver el contenido de `index.html`. 
* Pantallazo donde se pueda apreciar que accediendo a `c2` se puede ver el contenido de `index.html`. 
* Otro dos pantallazos (o uno) donde se vea accediendo a los contenedores después de modificar el fichero `index.html`.


### Trabajar con redes docker

1. Vamos a crear dos redes de ese tipo (BRIDGE) con los siguientes datos:

    **Red1**
    * Nombre: red1
    * Dirección de red: 172.28.0.0
    * Máscara de red: 255.255.0.0
    * Gateway: 172.28.0.1
    
    **Red2**
    * Nombre: red2
    * Es resto de los datos será proporcionados automáticamente por Docker.

2. Poner en ejecución un contenedor de la imagen `ubuntu:20.04` que tenga como hostname `host1`, como IP `172.28.0.10` y que esté conectado a la red1. Lo llamaremos `u1`.
3. Entrar en ese contenedor e instalar la aplicación ping (`apt update && apt install inetutils-ping`).
4. Poner en ejecución un contenedor de la imagen `ubuntu:20.04` que tenga como hostname `host2` y que esté conectado a la red2. En este caso será docker el que le de una IP correspondiente a esa red. Lo llamaremos `u2`.
5. Entrar en ese contenedor e instalar la aplicación ping (`apt update && apt install inetutils-ping`).

Deberás entregar los siguientes pantallazos comprimidos en un zip o en un documento pdf:

* Pantallazo donde se vea la configuración de red del contenedor u1. 
* Pantallazo donde se vea la configuración de red del contenedor u2. 
* Pantallazo donde desde cualquiera de los dos contenedores se pueda ver que no podemos hacer ping al otro ni por ip ni por nombre.
* Pantallazo  donde se pueda comprobar que si conectamos el contenedor `u1` a la red2 (con `docker network connect`), desde el contenedor u1, tenemos acceso al contenedor u2 mediante ping, tanto por nombre como por ip.