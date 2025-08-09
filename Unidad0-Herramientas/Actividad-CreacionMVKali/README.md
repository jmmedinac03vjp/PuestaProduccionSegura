# Actividad Unidad 0 - Creación de Máquina Virtual de Kali

Para realizar las actividades, siempre que podamos, vamos a utilizar una máquina virtual de Kali Linux.

El uso de la máquina virtual nos permite:

- Aislar, en cierto modo, el entorno de pruebas, de nuestra máquina anfitriona.
- Tener un entorno común, esto facilitará que todos tengamos un único entorno y será más fácil identificar los problemas que podamos tener, ya que nos deberían de surgir a todos.
- La MV es independiente de la plataforma, por lo que debería de funcionar igual en Sistemas Operativos Linux y Windows.

Los vídeos de ayuda a la resolución de actividades, estarán realizados en dicha máquina, por lo que si el alumnado utiliza otro medio/Sistema Operativo, será más difícil la detección y solución de problemas y errores.

Tenemos a nuestra disposición imágenes de `Kali` para diferentes Hypervisores. He decidido utilizar la herramienta `VMware` para la virtualización, por lo que se aconseja utilizarla también.

# [Objetivos](#objetivos)

# [Resultados de aprendizaje y Criterios de Evaluación](#resultados-de-aprendizaje-y-criterios-de-evaluación)

# [Desarrollo](#desarrollo)



# [Entrega](#entrega)

# Objetivos

- Ser capaz de intalar `VMWare Workstation` en nuestra máquina anfitriona.
- Crear Máquina Virtual de `Kali Linux` en `VMware Workstation`.

--- 

# Resultados de aprendizaje y Criterios de Evaluación

---

# Desarrollo

## Descarga de la imagen de la MV de Kali Linux

Desde la página oficial de Kali [https://www.kali.org](https://www.kali.org/get-kali/#kali-virtual-machines) tenemos disponibles imágenes preparadas para diferentes hypervisores.
Como he comentado antes, yo voy a utilizar el hypervisor `VMware`. Si eres usuario avanzado, utiliza el que quieras, si no lo eres tanto, te aconsejo utilizar el mismo que yo.

> ![](images/MV3.png)

Se descarga un archivo comprimido, deberás descomprimirlo.

## Descarga de VMware Workstation

- Acceder a la página de descarga de `VMware Workstation`. Lo puedes hacer buscando en `Google` o desde [este enlace](https://www.vmware.com/products/desktop-hypervisor/workstation-and-fusion).

> En la actualidad, `VMware` pertenece a `Broadcom` por lo que hay que crear una cuenta, acceder al área de `Descargas` y una vez allí ir al apartado de `Free Software Downloads`.
>
> ![](images/MV1.png)
>
> Una vez allí buscamos el producto `VMware Workstatio Pro`. Debería estar en  [este enlace](https://support.broadcom.com/group/ecx/productdownloads?subfamily=VMware%20Workstation%20Pro&freeDownloads=true).
> ![](images/MV2.png)
>
> Al pinchar el enlace comenzará la descarga.


## Instalación de VMware Workstation en Windows

Sencillo, tan sólo hacer doble clik sobre archivo descargado.

## Instalación de VMware Workstation en Linux

Nos situamos en el directorio donde hemos descargado el instalador, damos permiso de ejecución al archivo descargado, actualizamos las listas de repositorios, instalamos paquetes necesarios, y por último ejecutamos el instalador.


```bash
chmod x VMware-Player-*.bundle
sudo apt update
sudo apt install build-essential linux-headers-$(uname -r)
sudo ./VMware-Player-*.bundle
```
---

# Entrega
