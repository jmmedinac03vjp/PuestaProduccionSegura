# Índice
1. [Introducción](#introducción)
2. [Formatos de texto](#formatos-de-texto)
3. [Listas](#listas)
4. [Citas](#citas)
5. [Lista de tareas](#lista-de-tareas)
6. [Enlaces e imágenes](#enlaces-e-imágenes)
7. [Tablas](#tablas)
8. [Bloques de código](#bloques-de-código)

---

# Introducción
En este documento aprenderás a usar la sintaxis de Markdown para dar formato a un texto.  
Markdown es un lenguaje de marcado ligero muy usado en **documentación**, *notas rápidas* y ***readme de proyectos***.  
También permite ~~tachar texto~~ cuando es necesario.  

---

## Formatos de texto
En Markdown podemos usar:  
- *cursiva* para resaltar palabras  
- **negrita** para dar énfasis fuerte  
- ***negrita y cursiva*** a la vez para resaltar mucho más  
- ~~texto tachado~~ para mostrar elementos eliminados o cambios  

---

## Listas
Lista no ordenada:  
- Lenguajes de programación  
    - Python  
    - JavaScript  
- Sistemas operativos  
    - Linux  
    - Windows  

Lista ordenada:  
1. Crear una carpeta para tu proyecto  
2. Abrir el editor de texto  
3. Guardar el archivo con extensión `.md`  

---

## Citas
Las citas se usan para resaltar frases o referencias.  
Por ejemplo:  
> La simplicidad es la clave de la verdadera elegancia. — Coco Chanel  

---

## Lista de tareas
- [ ] Preparar el material de clase  
- [x] Escribir el texto base del ejercicio  
- [ ] Revisar y corregir el documento  

---

## Enlaces e imágenes
Aquí un enlace a la página web: [Google](https://www.google.com).  
Aquí un tienes un [enlace al documento de admisión  y matriculación a ciclos que se encuentra en la dirección https://doe.juntaex.es/pdfs/doe/2024/1000o/24061743.pdf`](https://doe.juntaex.es/pdfs/doe/2024/1000o/24061743.pdf).

 
Aquí tienes una imagen que está en la dirección <https://informatica.iesvalledeljerteplasencia.es/wp-content/uploads/2023/paginas/master/logos/CETI-vjp.png>. Debe de aparecer aquí justo debajo.   
![Logo](https://informatica.iesvalledeljerteplasencia.es/wp-content/uploads/2023/paginas/master/logos/CETI-vjp.png)  

---

## Tablas
A continuación una tabla con datos ficticios:  

| Nombre | Edad | Ciudad |
|--------|------|--------|
| Ana    | 23   | Madrid |
| Luis   | 30   | Barcelona |
| Sofía  | 28   | Valencia |

---

## Bloques de código
Ejemplo de comandos de `Bash` que nos sirven  para crear un repositorio en `Git` :

```bash
git init
git add .
git commit -m "Primer commit"
git branch -M main
git remote add origin URL_DEL_REPOSITORIO
git push -u origin main
```
