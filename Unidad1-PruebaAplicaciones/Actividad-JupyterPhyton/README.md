# Actividad - Jupyter y Phyton

Actividad de la Unidad 1 de Puesta en Producción Segura. Tabajaremos con lenguaje de programación Python y con Jupyter notebook.

**Índice**

[Objetivos](#objetivos)

[Resultados de aprendizaje y Criterios de Evaluación](#resultados-de-aprendizaje-y-criterios-de-evaluación)

[Desarrollo](#desarrollo)

[Entrega](#entrega)

---

# Objetivos

Tenemos varios objetivos:

- Conocer los diferentes elementos de código fuente en Python.
- Ser capaz de ejecturar y documentar fragmentos de código con `Jupyter-Notebook`.
- Realizar programas sencillos en Python.

--

# Resultados de aprendizaje y Criterios de Evaluación

Esta actividad se relaciona con el resultado de aprendizaje y criterios de evaluación RA1c.
---

# Desarrollo


> [Instalar Jupiter](#Instalacion-Jupyter)

> [Aprender a utilizar Jupyter](#Uso-Jupyter)

> [Conocer los elementos y sentencias de Python](#Python) 

---
## Instalacion Jupyter

Lee bien las instrucciones y ten en cuenta que tienes que hacer varias operaciones. Las que tienes a continuación son de un entorno Linux:

1. Instalamos, si no las tenemos, el paquete de python en su versión 3 y ``pip`` que es un gestor de paquetes escritos en python.
~~~
sudo apt install python3
sudo apt install pip
~~~

2. Instalamos Jupyter

~~~
#Si estás utilizando Kali quizá tengas que hacer
sudo apt install jupiter-notebook
# Si estás utilizando otro Linux:
pip install jupiter-lab
~~~
 

## Uso-Jupyter

Si no lo has visto, visualiza [este vídeo sobre Jupyter notebook](https://youtu.be/6Vr9ZUntCyE) 

> __Crea algún notobook para familiarizarte con el entorno.__
> __Añade en él algún campo tanto de código como de MarkDown__

## Python

Para aprender python puedes seguir cualquiera de los dos enlaces siguientes o puedes buscar alguno que te parezca mejor:

> En clase seguiremos [éste documento de `Jupyter Notebook` donde podemos ver los diferentes elementos de un programa](./ElementosPython.ipynb)

>[https://docs.python.org/3.10/contents.html](https://docs.python.org/3.10/contents.html)

>[https://protegermipc.net/2019/05/22/libro-python-basico-para-hackers-y-pentester](https://protegermipc.net/2019/05/22/libro-python-basico-para-hackers-y-pentester)

En el siguiente enlace tienes el Cheatsheet sobre markdown para que lo utilices al documentar tu notebook de Jupyter: [https://www.markdownguide.org/cheat-sheet/](https://www.markdownguide.org/cheat-sheet/). Recuerda que también tienes para ello una sección en el menú de ayuda de Jupyter.

>Crea un notebook en Jupyter documentado la creación de un programa en Python3 que simule un juego de tablero similar a "La Oca".
> En el juego participarán **cinco jugadores**.   
> El tablero es una lista de 25 casillas, numeradas del 0 (Inicio) al 24 (Meta).   
> Cada jugador está identificado por la inicial de su nombre (una letra mayúscula). El objetivo es llegar a la casilla Meta antes que el resto jugador.

**Reglas básicas:**
- Cada jugador elige una inicial única.
- Se decide aleatoriamente quién empieza.
- Los jugadores tiran un dado virtual (número aleatorio entre 1 y 6) en su turno.
- El jugador avanza tantas casillas como indique el dado.
- Si un jugador cae en la casilla del otro, el segundo vuelve a Inicio.
- El juego termina cuando un jugador llega o supera la casilla Meta (24).
- El tablero se muestra después de cada turno, indicando la posición de cada jugador.

---

# Entrega

>__Descarga el notebook realizado como "notebook de Jupyter" y lo envías a través de la plataforma.__
