# Análisis Dinámico de APK con MobSF y Genymotion: InsecureBankv2

Este repositorio documenta el proceso para realizar un análisis dinámico de la aplicación Android vulnerable **InsecureBankv2** usando **Mobile Security Framework (MobSF)** junto con el emulador **Genymotion**.

## Índice

1. [¿Qué es MobSF?](#1-qué-es-mobsf)  
2. [Obtener InsecureBankv2](#2-obtener-insecurebankv2)  
3. [Instalar MobSF](#3-instalar-mobsf)  
4. [Acceder a MobSF](#4-Acceder-a-mobsf)  
5. [¿Qué es Genymotion?](#5-qué-es-genymotion)  
6. [Instalar Genymotion](#6-instalar-genymotion)  
7. [Emular un dispositivo móvil](#7-emular-un-dispositivo-móvil-en-genymotion)  
8. [Ejecutar Back-end InsecureBankv2](#8-ejecutar-back-end-insecurebankv2)  
8. [Ejecutar InsecureBankv2 en el emulador](#9-ejecutar-insecurebankv2-en-el-emulador)  
9. [Poner en marcha el laboratorio](#10-poner-en-marcha-el-laboratorio)
9. [Análisis dinámico de la aplicación](#11-análisis-dinámico-de-la-aplicación)  
9.  [Interpretación de los resultados](#12-interpretación-de-los-resultados)

---
## 1. ¿Qué es MobSF?

**Mobile Security Framework (MobSF)** es una herramienta automatizada todo en uno para análisis de seguridad de aplicaciones móviles (Android/iOS/Windows). MobSF permite realizar análisis **estático**, **dinámico** y **basado en API**, y está especialmente diseñado para pruebas de seguridad móviles en entornos DevSecOps.

### Características principales:

- Análisis estático de APK, AAB, IPA y código fuente.
- Análisis dinámico (sandbox automatizado).
- Análisis de binarios y API REST.
- Informes detallados de seguridad y recomendaciones.

> Sitio oficial: https://mobsf.github.io/docs/

---

## 2. Obtener InsecureBankv2

**InsecureBankv2** es una aplicación vulnerable desarrollada con fines educativos para practicar análisis y explotación de fallos en apps móviles.

Puedes descargar la [Guía de uso de InsecureBankvs desde aquí.](files/InsecureBankv2UsageGuide.pdf)

### Pasos:

1. Clona el repositorio oficial:
   ```bash
   git clone https://github.com/dineshshetty/Android-InsecureBankv2.git
   ```

2. Compila el APK con Android Studio o utiliza una versión precompilada (si está disponible).
  Puedes descargarla desde el repositorio git del desarrollador: <https://github.com/dineshshetty/Android-InsecureBankv2/blob/master/InsecureBankv2.apk>
> ⚠️ **Nota:** Esta aplicación es intencionadamente insegura. No la instales en dispositivos personales o en entornos de producción.

---

## 3. Instalar MobSF

Puedes ejecutar MobSF localmente utilizando Docker o de forma manual. A continuación, se muestra el método recomendado (Docker):

### Opción 1: Usar Docker (recomendado)

```bash
git clone https://github.com/MobSF/Mobile-Security-Framework-MobSF.git
cd Mobile-Security-Framework-MobSF
docker build -t mobsf .
docker run -it -p 8000:8000 --name LabMobSF mobsf
```

También puedes hacerlo directamente  levantando la imagen de dockerhub:

```bash
docker run -it --rm  -p 8080:8000 --name MobSFopensecurity/mobile-security-framework-mobsf:latest
```
**Explicación de los parámetros**
- `--rm` Borramos las anteriores instancias de docker que se hayan ejecutado antes. Así no nos dá problema si hay alguna configuración anterior.
- `-it` Ejecutamos contenedor de forma interactiva. La máquina arrancará y quedará el terminal abierto. Así podremos ver los logs que van surgiendo en el contenedor.
- `-p 8000:8000` Redireccion de puertos. MobSF muestra su web por el puerto 8000. Nosotros lo redirigimos para que podamos acceder a él por el puerto 8000 de nuestra máquina anfitriona. Si quisiéramos verlo por el 8080 de nuestra máquina anfitriona por que estuviera ocupado el 8000, pondríamos `-p 8080:8000.
- `opensecurity/mobile-security-framework-mobsf:latest` La imagen docker que vamos a utilizar. Es del usuario `opensecurity` de `Hub.Docker.com` 
- `--name LabMobSF` es el nombre que queremos que tenga el contenedor docker.
![](images/image1.png)

De esta forma podemos levantar nuestro contenedor `MobSF` para realizar **análisis estáticos de código**. Si lo que deseamos hacer es un **análisis dinámico de código** necesitamos usar otro parámetro:
- `-e MOBSF_ANALYZER_IDENTIFIER=X.X.X.X:5555` Es el puerto por que se comunicará `ADB` con el emulador de la aplicación Android, donde X.X.X.X es la dirección IP del dispositivo virtual.

Luego levantaremos todo  el laboratorio por lo que puedes eliminar el contenedor:

```bash
docker ps
```

![](images/image34.png)

Nos muestra información de los contenedores levantados. Vemos como tenemos activo nuestro contenedor `LabMobSF`

Si queremos eliminar el contenedor:

```bash
docker rm -f LabMobSF
```


### Opción 2: Instalación manual

Sigue la guía oficial en: https://mobsf.github.io/docs/#/installation

---

## 4. Acceder a MobSF

Una vez iniciado MobSF (ya sea por Docker o manualmente), accede a través de tu navegador:

>  <http://localhost:8000>

En la pantalla de autenticación usamos el usuario `mobsf` y la contraseña por defecto: `mobsf`.

![](images/image2.png)


Verás la interfaz web de MobSF, lista para analizar APKs.

![](images/image3.png)
---

## 5. ¿Qué es Genymotion?

**Genymotion** es un emulador de Android que permite ejecutar máquinas virtuales de diferentes versiones y dispositivos. Es muy útil para realizar pruebas de seguridad móvil en entornos controlados.

> Sitio oficial: https://www.genymotion.com/

---

## 6. Instalar Genymotion

> Puedes descargar un documento de cómo descargar y crear un dispositivo virtual en [este documento de Rafael López García](files/InstalacionGenymotion.pdf).

1. Regístrate en [Genymotion](https://www.genymotion.com/account/create/). Deberás confirmar con el enlace enviado a tu correo electrónico
	
> En la versión gratuita nos ofrecen una versión trial de 30 días.

2. Descarga la versión para tu sistema operativo. En mi caso en `Linux` he descargado el archivo ` .run`.

![](images/image4.png)

3. Instálalo. En mi caso lo he copiado e instalado en la carpeta `/opt`:

```bash
sudo cp genymotion-3.9.0-linux_x64.run /opt/
sudo chmod 755 genymotion-3.9.0-linux_x64.run 
sudo ./genymotion-3.9.0-linux_x64.run 
```
Una vez instalado en tu equipo lánzalo desde el botón de `inicio` de tu SO.

![](images/image5.png)

> Si es necesario, puedes usarlo en Máquina Virtual.

4. Inicia sesión con tu cuenta de Genymotion.

![](images/image6.png)


> Si no te has registrado, tendrás que hacerlo en este momento para acceder a la aplicación.

Selecciona `Personal use`. Veremos el siguiente aviso:
 
![](images/image7.png)

5. Configurar el hypervisor como VirtualBox.

Por defecto el hypervisor que utiliza Genymotion es Quemu. El problema es que internamente crea una red NAT y por lo tanto nos puede dificultar la conexión con `MobSF`.

Para configurar nos vamos al apartado `Hypervisor` y seleccionamos el hipervisor `VirtualBox` en vez de `Quemu`.

![](images/image25.png)

La aplicación se reiniciará y nos aparece la pantalla de la aplicación

![](images/image27.png)

---

## 7. Emular un dispositivo móvil en Genymotion

1. Arrancamos Genymotion en nuestro Sistema operativo.

2. Crea una nueva máquina virtual Android (preferiblemente Android 5.0 con x86).
 
![](images/image8.png)

En los siguientes pasos podemos dejar todas las opciones tal y como están, salvo cambiarle el nombre al dispositivo, la versión de Android a la que nos interese e instalarle el teclado virutal. Aunque la opción “Enable Root Access” aparece desactivada, en principio sí que tendremos acceso de root.
- Seleccionamos un teléfono básico `Custom Phone`

![](images/image9.png)

- Cambiamos la versión de Android, seleccionando `Android 5`.

![](images/image10.png)

- Habilitamos teclado virtual en pantalla.

![](images/image11.png)

- !!IMPORTANTE¡¡ En la sección de "Hypervisor Options", configuramos la red del dispositivo en modo `Bridge`. Debemos seleccionar también la interfaz que estamos utilizando (wl0 para inalámbrica, en0 para cableada). 

- Al finalizar el proceso y darle a `Install` comenzará la creación del dispositivo. Tarda unos minutos.

3. Iniciar el dispositivo. Darle al símbolo de `play`.

![](images/image12.png)

Nos aparece el dispositivo.

![](images/image13.png)

### Comprobar conexión con dispositivo.

Para ver si hay conexión con el dispositivo creado:

1. Ver ip del dispositivo virtual. 
- Entramos en `Settings` o `Ajustes`

![](images/image28.png)

- Entramos en seccion `WIFI`

![](images/image29.png)

- Le damos a los tres puntos 

![](images/image30.png)

- Y finalmente en `Advanced` o `Avanzado`

![](images/image31.png)

Ya podremos ver los datos de la conexión: 

![](images/image32.png)

2. Probar conexión con ADB.

Para ver si nuestro equipo anfitrión conecta con el dispositivo virtual, desde el terminal de nuestro equipo:

```bash
adb connect X.X.X.X:5555
```
Siendo X.X.X.X la ip de nuestro dispositivo virtual. Si se establece la conexión aparecerá un mesnaje de `conected to X.X.X.X`

![](images/image33.png)

---

## 8. Ejecutar Back-end InsecureBankv2

InsecureBankv2 es una aplicación bancaria, por lo tanto tenemos:

- Aplicación Bancaria **Servidor** (Back-end).
- Aplicación Bancaria **Cliente**. En este caso APK para Android.


En este punto vamos a levantar la aplicación del servidor.

El desarrollador tiene creado un laboratorio en la carpeta `AndroLabServer`. En esencia vamos a:

- Crear un entorno virtual de Phyton para ejecutar el laboratorio.
- Instalar python (si no lo tienes instalado) y librerias de python.
- Ejecutar la aplicación.

La aplicación está escrito en Python 2.7, por lo que si tines instalado Python3 no se ejecutará correctamente.
Los módulos necesarios para arrancar la aplicación ya no vienen en los Linux modernos, sólo los incorpora hasta Ubuntu 22.04 LTS.

Para comprobar la versión de python que tenemos probamos con:

![](images/image19.png)

Como vemos en la imagen sólo nos detecta Python3. Al intentar ejecutar la aplicación nos da un error propio de que la función `print()` ha cambiado de `python2` a `python3`.

### Opción 1. Tienes instalado Python2

 Instalamos la librerías:

```bash
pip install -r requirements.txt
```

![](images/image15.png)

Aquí vemos cómo se ha instalado correctamente.

![](images/image16.png)

```bash
phyton app.py
```
### Opcion 2. Tienes instalado Python 3 :Instalación de Python2.7 y librerías necesarias.

Instalamos Python2 y las librerías necesarias.

```bash
sudo apt install python2
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
sudo python2 get-pip.py
pip2 install flask
pip2 install flask-sqlalchemy
pip2 install simplejson
pip2 install cherrypy
pip2 install web.py==0.51
pip2 install web.py
```
![](images/image18.png)


 E iniciamos el servidor:


```bash
 python2 app.py
```

![](images/image17.png)

---
  

## 9. Ejecutar InsecureBankv2 en el emulador

1. Instalamos la aplicación en el emulador arrastrando el paquete de la aplicación sobre el emulador:

![](images/image14.png)

2. Finalizada la instalación vemos cómo nos aparece la ventana de login.

![](images/image15.png)

3. Introducimos el usuario y la contraseña y pulsamos botón de `Login`.

> Estos son los usuarios válidos:
> - dinesh/Dinesh@123$
> - jack/Jack@123$

![](images/image20.png)

4. Introducimos dirección Ip del Servidor.

Si lo hemos creado en nuestro equipo tan sólo tenemos que ver la ip de nuestro equipo y ponerla. Por defecto usamos el puerto 8888.

![](images/image21.png)

Después de darle al botón de `Submit` accedemos a la aplicación:

![](images/image22.png)

En cualquier momento podemos cambiar los datos del servidor dándole a los tres puntos, en el apartado de `Preferencias`

![](images/image36.png)

---
## 10. Poner en marcha el laboratorio

1. Lanza la ejecución del servidor de `InsecureBank`
Colocado en la carpeta `AndroLabServer`

```bash
phyton2 app.py
# Si no tienes python3 será python en vez de phyton2
#phyton app.py
```

1. Abre el emulador `Genymotion`
1. Inicia el dispositivo virtual que hemos creado en `Genymotion` 
1. Anota la dirección Ip que coge el dispositivo virtual
![](images/image35.png)
En este caso es la 192.168.1.137. ¡¡¡OJO¡¡ que esta ip no tiene que ser siempre la misma en diferentes ejecuciones.
1. Ejecuta la aplicación `InsecureBank` en el navegador. Si la tienes instalada anteriormente tan sólo tienes que buscarla en el dispositivo virtual, y sino, arrastra la apk sobre el emulador.
1. Introduce usuario y contraseña `jack` y `jack@123$`
1. Lo siguiente es poner la ip de la máquina donde se ejecuta el servidor de `InsecureBank`.Recuerda que lo puedes hacer en `Preferencias` de la APP. En nuestro caso la ip de nuestra máquina anfitriona. El puerto si no lo hemos cambiado sigue siendo `8888`  
1. Levanta MobSF: !!!OJO¡¡¡ que tendrás que cambiar la ip asociada a la variable `MOBSF_ANALYZER_IDENTIFIER`, en el comando docker de abajo.

```bash
docker run -it --rm -e MOBSF_ANALYZER_IDENTIFIER=192.168.1.137:5555 -p 8000:8000 opensecurity/mobile-security-framework-mobsf:latest
```

1. Accede a `MobSF`

<http://localhost:8080/>

---
## 11. Análisis dinámico de la aplicación

1. Accede a MobSF en `http://localhost:8000`.

![](images/image24.png)

2. Arrastramos la apk sobre el emulador.

![](images/image23.png)
 
3. Selecciona la opción **Dynamic Analyzer**.

![](images/image37.png)

3. Asegúrate de que MobSF detecta el dispositivo emulado vía ADB.

4. Carga el APK de InsecureBankv2.

Vemos como esta conectado correctamente con nuestro dispositivo virtual.

![](images/image38.png)

1. Vemos las aplicaciones detectadas por el analizador dinámico.
Como nos interesa MobSF, pulsamos en ella en `Iniciar Análisis dinámico` 

![](images/image39.png)

5. Sigue las instrucciones para iniciar el análisis dinámico.

> MobSF lanzará la app en el emulador y empezará a registrar comportamiento, tráfico, uso de permisos, etc.

![](images/image41.png)

-


--

## 12. Interpretación de los resultados

El informe dinámico incluirá información como:

- **Permisos en tiempo de ejecución**.
- **Tráfico de red y endpoints detectados**.
- **Interacciones con el sistema**.
- **Análisis de logs, broadcasts, servicios, etc.**
- **Captura de tráfico HTTPS (si está configurado con proxy o CA)**.

---
## Ejercicios propuestos

### 2. Ejercicio 1: Captura de credenciales

1. Inicia sesión desde la app:
   ```
   Usuario: test
   Contraseña: test123
   ```
2. Observa en MobSF:
   - **Pestaña Network**: ¿Se transmiten credenciales en texto claro?
   - **Logcat**: ¿Se imprimen datos sensibles en consola?

---

### 3. Ejercicio 2: Almacenamiento inseguro

1. Completa acciones en la app (login, ver saldo, transferencias).
2. En MobSF, ve a **"File System"** y revisa:
   - `/data/data/com.android.insecurebankv2/`
   - `/sdcard/`

3. Busca archivos `.xml`, `.db`, `.txt` con datos sensibles.

---

### 4. Ejercicio 3: Análisis de tráfico HTTPS (opcional)

1. Configura Burp Suite como proxy en el host.
2. Ajusta el proxy del emulador Genymotion.
3. Instala el certificado CA de Burp en el emulador.
4. Navega por la app y captura tráfico cifrado.

---

### 5. Ejercicio 4: Análisis de APIs

1. Interactúa con la app desde el emulador.
2. Revisa la pestaña **API Monitor** en MobSF.
3. Copia URLs de API y prueba:
   - Inyección SQL
   - Fuzzing de parámetros
   - Peticiones sin autenticación

---

### 6. Ejercicio 5: Comunicación entre componentes

1. Lanza una Activity manualmente con ADB:
   ```bash
   adb shell am start -n com.android.insecurebankv2/.SomeActivity
   ```

2. Revisa si se puede acceder a componentes protegidos.
3. Revisa el informe de ICC en MobSF.

---

### 7. Conclusión

Anota vulnerabilidades encontradas y qué controles de seguridad faltan.

### Preguntas guía:
- ¿Qué datos se almacenan sin cifrar?
- ¿Hay tráfico HTTP inseguro?
- ¿Qué endpoints carecen de autenticación o validación?
- ¿Se pueden explotar componentes internos de la app?

---


## 📘 Recursos adicionales

- [MobSF Documentation](https://mobsf.github.io/docs/)
- [Genymotion User Guide](https://docs.genymotion.com/)
- [InsecureBankv2 GitHub](https://github.com/dineshshetty/Android-InsecureBankv2)
- [Guía de uso de InsecureBankvs desde aquí.](files/InsecureBankv2UsageGuide.pdf)
- [Manual de uso de Genymotio de Rafa López](files/InstalacionGenymotion.pdf)
- [Tutorial análisis de vulnerabilidades de http://jaymonsecurity.es](https://jaymonsecurity.es/analisis-vulnerabilidades-app-android2/)
---

## ⚠️ Disclaimer

Este proyecto es solo para fines educativos. No uses estas herramientas sobre apps sin autorización expresa.

---

## Autor

Repositorio creado por [TuNombre], para prácticas de análisis dinámico de seguridad móvil en el contexto de PPS (Prácticas Profesionales Supervisadas).
