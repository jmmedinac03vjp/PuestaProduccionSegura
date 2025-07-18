# Actividad- Explotación y Mitigación de Remote File Inclusion (RFI)

Tenemos como objetivo:

> - Ver cómo se pueden hacer ataques Inclusión de Archivos Remotosn (RFI).
>
> - Analizar el código de la aplicación que permite ataques de Inclusión de Archivos Remotosn (RFI).
>
> - Implementar diferentes modificaciones del codigo para aplicar mitigaciones o soluciones.

## ¿Qué es Remote File Include?
---

La vulnerabilidad de Inclusión de archivos permite a un atacante incluir un archivo, generalmente explotando un mecanismo “dynamic file inclusion” implementado en la aplicación de destino. La vulnerabilidad se produce debido al uso de la entrada suministrada por el usuario sin la validación adecuada.

Esto puede conducir a algo como la salida del contenido del archivo, pero dependiendo de la gravedad, también puede conducir a:

- Ejecución de código en el servidor web

- Ejecución de código en el lado del cliente, como JavaScript, que puede conducir a otros ataques, como secuencias de comandos en sitios cruzados (XSS)

- Denegación de Servicio (DoS)

- Divulgación de Información Sensible

Remote File Inclusion (también conocido como RFI) es el proceso de incluir archivos remotos a través de la explotación de procedimientos de inclusión vulnerables implementados en la aplicación. Esta vulnerabilidad se produce, por ejemplo, cuando una página recibe, como entrada, la ruta al archivo que tiene que incluirse y esta entrada no se desinfecta correctamente, lo que permite inyectar una URL externa. Aunque la mayoría de los ejemplos apuntan a scripts PHP vulnerables, debemos tener en cuenta que también es común en otras tecnologías como JSP, ASP y otras.
 
## ACTIVIDADES A REALIZAR
---
> Lee detenidamente la sección de vulnerabilidades de subida de archivos.  de la página de PortWigger <https://portswigger.net/web-security/file-upload>
>
> Lee el siguiente [documento sobre Explotación y Mitigación de ataques de Remote Code Execution](./files/ExplotacionYMitigacionRFI.pdf)
> 
> También y como marco de referencia, tienes [ la sección de correspondiente de ataque de inclusión de archivos remotos de la **Proyecto Web Security Testing Guide** (WSTG) del proyecto **OWASP**.](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/11.2-Testing_for_Remote_File_Inclusion)
>

### Configuración para deshabilitar la seguridad en PHP 8.2 (sólo para pruebas)

Para poder realizar la actividad vamos a deshabilitar la seguridad y así poder trabajar la vulnerabilidad correctamente. Lo realizaremos cambiando la configuración de PHP.

Para ello nos conectamos a nuestro contenedor si estás utilizando es escenario con docker:

~~~
docker exec -it lamp-php83 /bin/bash
~~~

 y una vez que nos hemos conectado, guardamos una copia de seguridad del archivo de configuración para volverlo a restaurar al final de la actividad:

~~~
cd /usr/local/etc/php/
cp php.ini php.ini-original
nano php.ini
~~~

Añadimos al final las variables indicadas:

~~~
disable_functions =
allow_url_include = On
allow_url_fopen = On
open_basedir = 
~~~

Una vez cambiada la configuración, reiniciamos el servicio o en el caso de que utilicemos docker, reiniciamos el contenedor:

~~~
docker-compose restart webserver
~~~

![](images/rfi1.png)


Aquí puedes encontrar el fichero de configuración [php.ini](files/php.ini.rfi).

¿Qué hacemos con estas configuraciones?

1. Elimina todas las funciones deshabilitadas (disable_functions vacío).

2. Habilita la inclusión de archivos remotos (allow_url_include = On).

3. Habilita file_get_contents() para URLs externas (allow_url_fopen = On).

4. Desactiva open_basedir para permitir la ejecución en cualquier directorio.

## Código vulnerable
---

Tenemos el siguiente código vulnerable al cual le tenemos que indicar un fichero a subir al servidor:
~~~
?php
// Verificar si se ha pasado un archivo por parámetro
if (isset($_GET['file'])) {
        $file = $_GET['file'];
        include($file);
}

?>
<form method="GET">
        <input type="text" name="file" placeholder="Usuario">
        <button type="submit">Subir Archivo</button>
</form>

~~~ 

![](images/rfi3.png)

### Explotación de RFI
---
Para comprobar la explotación de RFI vamos a crear un archivo malicioso exploit.php en un servidor controlado por el atacante.

En nuestro caso [exploit.php](files/exploit.php) lo vamos a colocar en nuestro servidor. Tendrá el siguiente contenido:


~~~
<?php
echo "¡Servidor comprometido!";
// Código malicioso, como una web shell o un backdoor
?>
~~~


En esta ocasión sólo nos mostrará un mensaje, pero podría hacer muchas cosas más.

Para ejecutarlo a través de la aplicación vulnerable colocando su dirección en nuestro campo
![](images/rfi3.png)


o bien concatenamos su dirección a la de nuestro archivo rfi.php:


~~~
http://localhost/rfi.php?file=http://localhost/exploit.php
~~~

Si el código del atacante se ejecuta en el servidor víctima, significa que la aplicación es vulnerable.

![](images/rfi2.png)

**Posibles efectos del ataque:**

- Acceso no autorizado al servidor.

- Robo de datos sensibles.

- Modificación o eliminación de archivos del sistema.

- Instalación de malware o puertas traseras (backdoors).

## Mitigación de RFI
---

La solución más efectiva para eliminar las vulnerabilidades de inclusión de archivos es evitar pasar la entrada enviada por el usuario a cualquier API de sistema de archivos/marco. Si esto no es posible, la aplicación puede mantener una lista de permisos de archivos que puede incluir la página y, a continuación, utilizar un identificador (por ejemplo, el número de índice) para acceder al archivo seleccionado. Cualquier solicitud que contenga un identificador no válido debe rechazarse para que no haya oportunidad de que los usuarios maliciosos manipulen la ruta. Mira el [Archivo de Hoja de Trucos para buenas prácticas de seguridad](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) en este tema.

Vamos realizando operaciones.

**Bloquear la inclusión de URLs externas**

En lugar de permitir cualquier entrada sin validación, se debe bloquear la inclusión de archivos remotos:

~~~
<?php
// Verificar si se ha pasado un archivo por parámetro
if (isset($_GET['file'])) {
        $file = $_GET['file'];
        // Bloquear URLs externas
        if (filter_var($file, FILTER_VALIDATE_URL)) {
                die("Incluir archivos remotos está prohibido.");
        }
        // Incluir el archivo sin más restricciones (Aún vulnerable a LFI)
        include($file);
}

?>
<form method="GET">
        <input type="text" name="file" placeholder="Usuario">
        <button type="submit">Iniciar Sesión</button>
</form>
~~~
Como vemos ya no nos deja meter direcciones url, ya que aplicamos un filtro de validación de URLs.

![](images/rfi3.png)

Sin embargo, esta solución no es suficiente, ya que aún permite archivos locales maliciosos.

**Restringir las rutas de inclusión**

La siguiente aproximación, sería limitar la inclusión de archivos solo a una lista de archivos específicos dentro del servidor:
~~~
<?php
// Verificar si se ha pasado un archivo por parámetro
if (isset($_GET['file'])) {
        $file = $_GET['file'];
        // Lista blanca de archivos permitidos
        $whitelist = ['file1.php', 'files/file2.php'];
        if (!in_array($file, $whitelist)) {
                die("Acceso denegado.");
        }
        // Incluir solo archivos de la lista blanca
        include($file);
}

?>
<form method="GET">
        <input type="text" name="file" placeholder="Usuario">
        <button type="submit">Iniciar Sesión</button>
</form>
~~~

En esta ocasión nos dejaría el acceso a los ficheros file1.php y a /files/file2.php

**Usar rutas absolutas y sanitización**

Podemos ir un paso más allá asegurándonos que solo se incluyan archivos desde una ubicación específica, en este caso el mismo directorio que el script:

~~~
<?php
// Establecemos el directorio permitido en el mismo directorio del script
$baseDir = __DIR__ . DIRECTORY_SEPARATOR;

if (isset($_GET['file'])) {
    $file = $_GET['file'];

    // Normalizamos la ruta para evitar ataques con '../'
    $filePath = realpath($baseDir . $file);
    // Verificamos si el archivo está dentro del directorio permitido
    if ($filePath === false || strpos($filePath, $baseDir) !== 0) {
        die("Acceso denegado.");
    }

    // Verificamos que el archivo realmente existe
    if (!file_exists($filePath)) {
        die("El archivo no existe.");
    }
    include($file);

}
?>
<form method="GET">
        <input type="text" name="file" placeholder="Usuario">
        <button type="submit">Iniciar Sesión</button>
</form>

~~~

Ahora sólo nos dejara incluir archivos del directorio actual.

**Deshabilitar allow_url_include en php.ini**

Para prevenir la inclusión remota de archivos en PHP podemos configurar el servidor para que acepte únicamente archivos locales y no archivos remotos.

Esto, como hemos visto anteriormente se hace configurando la variable allow_url_include en el archivo php.ini. Esta opción previene ataques RFI globalmente.
 

~~~ 
allow_url_include = Off
~~~


### **Código seguro**
---

Aquí está el código securizado:

~~~
?php
// Establecemos el directorio permitido en el mismo directorio del script
$baseDir = __DIR__ . DIRECTORY_SEPARATOR;
$whitelist = ['file1.php', 'file2.php'];

if (isset($_GET['file'])) {
        $file = $_GET['file'];
        // Bloquear URLs externas
        if (filter_var($file, FILTER_VALIDATE_URL)) {
                die("Incluir archivos remotos está prohibido.");
        }
        // Normalizamos la ruta para evitar ataques con '../'
        $filePath = realpath($baseDir . $file);
        // Verificamos si el archivo está dentro del directorio permitido
        if ($filePath === false || strpos($filePath, $baseDir) !== 0) {
            die("Acceso denegado.");
        }
       // Lista blanca de archivos permitidos
        if (!in_array($file, $whitelist)) {
                die("Acceso denegado.");
        }
 
        // Verificamos que el archivo realmente existe
        if (!file_exists($filePath)) {
            die("El archivo no existe.");
        }
        include($file);

}
?>
<form method="GET">
        <input type="text" name="file" placeholder="Usuario">
        <button type="submit">Iniciar Sesión</button>
</form>

~~~
🔒 Medidas de seguridad implementadas

- Bloqueadas URLs externas.
- Sanitización de ruta (eliminar ../ y evitar que el archivo no tenga caracteres maliciosos).
- Uso de lista blanca de archivos.

### Dejando todo en orden
----

Recuerda volver a poner el archivo php.ini original:

~~~
cd /usr/local/etc/php/
cp php.ini-original php.ini
~~~


## ENTREGA

> __Realiza las operaciones indicadas__

> __Crea un repositorio  con nombre PPS-Unidad3Actividad9-Tu-Nombre donde documentes la realización de ellos.__

> No te olvides de documentarlo convenientemente con explicaciones, capturas de pantalla, etc.

> __Sube a la plataforma, tanto el repositorio comprimido como la dirección https a tu repositorio de Github.__

