
# Síntaxis de MarkDown


**Índice**
[Encabezados](#encabezados)
[Estilos de texto](#estilos-de-texto)
[Entrecomillado de texto](#entrecomillado-de-texto)
[Código de cita](#codigo-de-cita)
[Vínculos](#vinculos)
# [Saltos de línea](#saltos-de-linea)
# [Imágenes](#imagenes)
# [Listas](#listas)
# [Listas de tareas](#listas-de-tareas)
# [Usar emojis](#usar-emojis)
# [Párrafos](#parrafos)
# [Notas al pie](#notas-al-pie)
# [Alertas](#alertas)
# [Ocultar el contenido con comentarios](#ocultar-el-contenido-con-comentarios)
# [Ignorar formato de Markdown](#ignoranr-formato-de-markdown)
# [Tablas](#tablas)
# [Secciones contraidas](#secciones-contraidas)
# [Crear y resaltar bloques de código](#crear-y-resaltar-bloques-de-codigo)
# [Diagramas](#diagramas)
# [Creación de mapas GeoJSON y TopoJSON](#creacion-de-mapas-geojson-y-topojson)
# [Expresiones matemáticas](#expresiones-matematicas)
# [Listas de tareas](#listas-de-tareas)
# [Referencias](#referencias)

---

# Encabezados

Para crear un encabezado, agrega entre uno y seis símbolos # antes del encabezado del texto. El número de # que utilices determinará el nivel jerárquico y el tamaño tipográfico del encabezado.

```markdown
# A first-level heading
## A second-level heading
### A third-level heading
```

# A first-level heading
## A second-level heading
### A third-level heading


---


# [Estilos de texto](#estilos-de-texto)

Puedes indicar énfasis con texto en negrita, cursiva, tachado, o de subíndice o superíndice en los campos de comentarios y archivos `.md`.

| Estilo | Sintaxis | Métodos abreviados de teclado | Ejemplo | Resultados |
| --- | --- | --- | --- | --- |
| Bold | `** **` o `__ __` | Command+B (Mac) o Ctrl+B (Windows/Linux) | `**This is bold text**` | **Esto es texto en negrita**. |
| Cursiva | `* *` o `_ _` | Command+I (Mac) o CtrI\+ (Windows/Linux) | `_This text is italicized_` | _Este texto está en cursiva_ |
| Tachado | `~~ ~~` o `~ ~` | Ninguno | `~~This was mistaken text~~` | ~Este texto está equivocado~ |
| Cursiva en negrita y anidada | `** **` y `_ _` | Ninguno | `**This text is _extremely_ important**` | **Este texto es _extremadamente_ importante** |
| Todo en negrita y cursiva | `*** ***` | Ninguno | `***All this text is important***` | _**Todo este texto es importante**_ |
| Subscript | `<sub> </sub>` | Ninguno | `This is a <sub>subscript</sub> text` | Se trata de un texto de subíndice |
| Superscript | `<sup> </sup>` | Ninguno | `This is a <sup>superscript</sup> text` | Se trata de un texto de superíndice |
| Subrayado | `<ins> </ins>` | Ninguno | `This is an <ins>underlined</ins> text` | Se trata de un texto subrayado |


# [Entrecomillado de texto](#entrecomillado-de-texto)

Puede entrecomillar texto con \>.

```markdown
Text that is not a quote

> Text that is a quote
```

Text that is not a quote

> Text that is a quote

Al texto entre comillas se le aplica sangría con una línea vertical en la izquierda y se muestra mediante texto en color gris.




# [Código de cita](#código-de-cita)

Puedes indicar un código o un comando dentro de un enunciado con comillas invertidas. El texto dentro de las comillas invertidas no será formateado. También puedes presionar el método abreviado de teclado Comando+E (Mac) o Ctrl+E (Windows o Linux) para insertar las comillas invertidas de bloque de código en una línea de Markdown.

```markdown
Use `git status` to list all new or modified files that haven't yet been committed.
```

Use `git status` to list all new or modified files that haven't yet been committed.


Para formatear código o texto en su propio bloque distintivo, usa comillas invertidas triples.

````markdown
Some basic Git commands are:
```git
git status
git add
git commit
```
````

Some basic Git commands are:
```
git status
git add
git commit
```

>Nota
>
>Observa cómo junto con las tres comillas invertidas podemos poner el lenguaje del código. Así podemos poner ```python  para códigos en lenguaje python.

También podemos utilizar en vez de las comillas invertidas ``` cejillas, ~~~. De esta forma obtenemos un bloque de código donde nos aparecerán opciones de copiar el bloque.

```
~~~
git status
git add
git commit
~~~
```

~~~
git status
git add
git commit
~~~


# [Vínculos](#vinculos)

Puede crear un vínculo en línea escribiendo su texto entre corchetes `[ ]` y escribiendo la URL entre paréntesis `( )`. También puede usar el método abreviado de teclado Command+K para crear un vínculo. Cuando haya seleccionado texto, puede pegar una dirección URL del Portapapeles para crear automáticamente un vínculo a partir de la selección.

También puedes crear un hipervínculo de Markdown resaltando el texto y usando el método abreviado de teclado Comando+V. Si quieres reemplazar el texto por el vínculo, usa el método abreviado de teclado Comando+Mayús+V.

`This site was built using [GitHub Pages](https://pages.github.com/).`


This site was built using [GitHub Pages](https://pages.github.com/).

## [Enlaces de sección](#section-links)

Puede vincular directamente a cualquier sección que tenga un encabezado. Para ver el delimitador generado automáticamente en un archivo representado, mantenga el puntero sobre el encabezado de sección para exponer el icono de y haga clic en el icono para mostrar el delimitador en el explorador.



Si necesitas determinar el ancla de un encabezado en un archivo que estás editando, puede usar las siguientes reglas básicas:

*   Las letras se convierten a minúsculas.
*   Los espacios se reemplazan por guiones (`-`). Se quitan cualquier otro espacio en blanco o caracteres de puntuación.
*   Se quitan los espacios en blanco iniciales y finales.
*   Se quita el formato de marcado, dejando solo el contenido (por ejemplo, `_italics_` se convierte en `italics`).
*   Si el ancla generada automáticamente para un encabezado es idéntico a una ancla anterior en el mismo documento, se genera un identificador único anexando un guión y un entero de incremento automático.


El bloque de código siguiente muestra las reglas básicas que se usan para generar anclas a partir de encabezados en contenido representado.

```markdown
# Example headings

## Sample Section

## This'll be a _Helpful_ Section About the Greek Letter Θ!
A heading containing characters not allowed in fragments, UTF-8 characters, two consecutive spaces between the first and second words, and formatting.

## This heading is not unique in the file

TEXT 1

## This heading is not unique in the file

TEXT 2

# Links to the example headings above

Link to the sample section: [Link Text](#sample-section).

Link to the helpful section: [Link Text](#thisll-be-a-helpful-section-about-the-greek-letter-Θ).

Link to the first non-unique section: [Link Text](#this-heading-is-not-unique-in-the-file).

Link to the second non-unique section: [Link Text](#this-heading-is-not-unique-in-the-file-1).
```

# Example headings

## Sample Section

## This'll be a _Helpful_ Section About the Greek Letter Θ!
A heading containing characters not allowed in fragments, UTF-8 characters, two consecutive spaces between the first and second words, and formatting.

## This heading is not unique in the file

TEXT 1

## This heading is not unique in the file

TEXT 2

# Links to the example headings above

Link to the sample section: [Link Text](#sample-section).

Link to the helpful section: [Link Text](#thisll-be-a-helpful-section-about-the-greek-letter-Θ).

Link to the first non-unique section: [Link Text](#this-heading-is-not-unique-in-the-file).

Link to the second non-unique section: [Link Text](#this-heading-is-not-unique-in-the-file-1).
Nota:

Si edita un encabezado o cambia el orden de los encabezados con anclas "idénticas", también deberá actualizar los vínculos a esos encabezados, ya que las anclas cambiarán.

## [Vínculos relativos](#relative-links)

Puedes definir enlaces relativos y rutas de imagen en los archivos representados para ayudar a que los lectores naveguen hasta otros archivos de tu repositorio.

Un enlace relativo es un enlace que es relativo al archivo actual. Por ejemplo, si tiene un archivo Léame en la raíz del repositorio y tiene otro archivo en _docs/CONTRIBUTING.md_, el vínculo relativo a _CONTRIBUTING.md_ en el archivo Léame podría tener este aspecto:

```text
[Guía de ciberataques](./osi-guia-ciberataques.pdf)
```

[Guía de ciberataques](./osi-guia-ciberataques.pdf)

Los enlaces relativos son más sencillos para los usuarios que clonan tu repositorio. Puede que los enlaces absolutos no funcionen en los clones de tu repositorio. Recomendamos usar enlaces relativos para consultar los archivos dentro de tu repositorio.

## [Anclas personalizadas](#custom-anchors)

Puede usar etiquetas de anclaje HTML estándar (`<a name="unique-anchor-name"></a>`) para crear puntos de anclaje de navegación para cualquier ubicación del documento. Para evitar referencias ambiguas, use un esquema de nomenclatura único para etiquetas de anclaje, como agregar un prefijo al valor de atributo `name`.

>Nota:
>
>Las anclas personalizadas no se incluirán en el esquema o tabla de contenido del documento.

Puedes vincular a una ancla personalizada mediante el valor de atributo `name` que proporcionó el ancla. La sintaxis es exactamente la misma que cuando se vincula a una ancla que se genera automáticamente para un encabezado.

Por ejemplo:

```markdown
# Section Heading

Some body text of this section.

<a name="my-custom-anchor-point"></a>
Some text I want to provide a direct link to, but which doesn't have its own heading.

(… more content…)

[A link to that custom anchor](#my-custom-anchor-point)
```

# Section Heading

Some body text of this section.

<a name="my-custom-anchor-point"></a>
Some text I want to provide a direct link to, but which doesn't have its own heading.

(… more content…)

[A link to that custom anchor](#my-custom-anchor-point)

> Sugerencia
>
> Las anclas personalizados no se tienen en cuenta por el comportamiento automático de nomenclatura y numeración de vínculos de encabezado automático.


# [Saltos de línea](#saltos-de-linea)

Si está escribiendo en problemas, en solicitudes de extracción o en discusiones de un repositorio, GitHub generará un salto de línea automáticamente:

```markdown
This example
Will span two lines
```


Sin embargo, si está escribiendo en un archivo .md, el ejemplo anterior se representaría en una línea sin salto. 

This example
Will span two lines

Para crear un salto de línea en un archivo .md, deberá incluir uno de los elementos siguientes:

*   Incluya dos espacios al final de la primera línea.
    
    This example  
    Will span two lines
    

This example  
Will span two lines

*   Incluya una barra diagonal inversa al final de la primera línea.
    
    ```markdown
    This example\
    Will span two lines
    ```
    
This example\
Will span two lines

*   Incluya una etiqueta de salto de una sola línea HTML al final de la primera línea.
    
    ```markdown
    This example<br/>
    Will span two lines
    ```

This example<br/>
Will span two lines    


Si deja una línea en blanco entre dos líneas, tanto los archivos .md como Markdown en problemas, en solicitudes de extracción y en discusiones mostrarán las dos líneas separadas por la línea en blanco:

```markdown
This example

Will have a blank line separating both lines
```
This example

Will have a blank line separating both lines


# [Imágenes](#imagenes)

Puede mostrar una imagen agregando ! y ajustar el texto alternativo en `[ ]`. El texto alternativo es un texto corto equivalente a la información de la imagen. Luego, escribe el vínculo de la imagen entre paréntesis `()`.

```
![Sello excelencia IES Valle del Jerte de Plasencia](https://informatica.iesvalledeljerteplasencia.es/wp-content/uploads/2023/paginas/proyectos/excelencia/sello-excelencia.png)
```

![Sello excelencia IES Valle del Jerte de Plasencia](https://informatica.iesvalledeljerteplasencia.es/wp-content/uploads/2023/paginas/proyectos/excelencia/sello-excelencia.png)

> Nota:  
> Cuando quieras mostrar una imagen incluida en el repositorio, usa vínculos relativos en vez de absolutos.

```
![Sello excelencia IES Valle del Jerte de Plasencia](./sello-excelencia.png)
```

![Sello excelencia IES Valle del Jerte de Plasencia](./sello-excelencia.png)


Aquí tienes algunos ejemplos para utilizar enlaces relativos para mostrar una imagen.

| Context | Enlace Relativo |
| --- | --- |
| En un archivo `.md` de la misma rama | `/assets/images/electrocat.png` |
| En un archivo `.md` de otra rama | `/../main/assets/images/electrocat.png` |
| En propuestas, solicitudes de cambio y comentarios del repositorio | `../blob/main/assets/images/electrocat.png?raw=true` |
| En un archivo `.md` de otro repositorio | `/../../../../github/docs/blob/main/assets/images/electrocat.png` |
| En propuestas, solicitudes de cambios y comentarios de otro repositorio | `../../../github/docs/blob/main/assets/images/electrocat.png?raw=true` |

> Nota:  
> Los últimos dos vínculos relativos de la tabla anterior funcionarán únicamente para las imágenes de repositorios privados si el lector tiene (como mínimo) acceso de lectura.

Para obtener más información, consulte [Vínculos relativos](#relative-links).

### [Elemento de imagen](#the-picture-element)

Se admite el elemento HTML `<picture>`.

# [Listas](#listas)

Puedes crear una lista sin ordenar. Para ello, coloca \-, \* o + antes de una o más líneas de texto.

```markdown
- George Washington
* John Adams
+ Thomas Jefferson
```

- George Washington
* John Adams
+ Thomas Jefferson


![Captura de pantalla de GitHub Markdown en la que se muestra una lista con viñetas de los nombres de los tres primeros presidentes de Estados Unidos.](/assets/cb-7925/images/help/writing/unordered-list-rendered.png)

Para ordenar tu lista, antecede cada línea con un número.

```markdown
1. James Madison
2. James Monroe
3. John Quincy Adams
```

1. James Madison
2. James Monroe
3. John Quincy Adams



## [Listas anidadas](#listas-anidadas)

Puedes crear una lista anidada al dejar sangría en uno o más elementos de la lista debajo de otro elemento.

Para crear una lista anidada mediante el editor web en GitHub o un editor de texto que use una fuente monoespaciada, como [Visual Studio Code](https://code.visualstudio.com/), puedes alinear la lista visualmente. Escribe los caracteres con espacio frente al elemento de la lista anidada hasta que el carácter del marcador de lista (\- o \*) se encuentre directamente debajo del primer carácter del texto en el elemento que se encuentra debajo.

```markdown
1. First list item
   - First nested list item
     - Second nested list item
```

1. First list item
   - First nested list item
     - Second nested list item

> Nota:   
> En el editor web, puedes aplicar o desaplicar sangría en una o varias líneas de texto si resaltas primero las líneas deseadas y, a continuación, usas Tab o mayús+Tab respectivamente.

Para crear una lista anidada en el editor de comentarios de GitHub, que no usa una fuente monoespaciada, puedes observar el elemento de lista inmediatamente anterior a la lista anidada y contar el número de caracteres que aparecen antes del contenido del elemento. Luego escribe ese número de caracteres de espacio frente al elemento de la lista anidada.

En este ejemplo, podría agregar un elemento de lista anidada bajo el elemento de lista `100. First list item` mediante la aplicación de sangría de mínimo cinco espacios en el elemento de lista anidada, ya que hay cinco caracteres (`100.` ) antes de `First list item`.

```markdown
100. First list item
     - First nested list item
```

100. First list item
     - First nested list item




Puedes crear múltiples niveles de listas anidadas mediante el mismo método. Por ejemplo, dado que el primer elemento de lista anidada tiene siete caracteres (`␣␣␣␣␣-␣`) antes del contenido `First nested list item` de la lista anidada, tendrás que aplicar sangría en el segundo elemento de lista anidada con al menos dos caracteres más (mínimo 9 espacios).

```markdown
100. First list item
     - First nested list item
       - Second nested list item
```

100. First list item
     - First nested list item
       - Second nested list item


Para obtener más ejemplos, consulte las [especificaciones de GitHub Flavored Markdwon](https://github.github.com/gfm/#example-265).


# [Listas de tareas](#listas-de-tareas)

Para crear una lista de tareas, debe añadir como prefijo un guion y espacio, seguido de `[ ]` a los elementos de la lista. Para marcar una tarea como completada, use `[x]`.

```markdown
- [x] #739
- [ ] https://github.com/octo-org/octo-repo/issues/740
- [ ] Add delight to the experience when all tasks are complete :tada:
```

- [x] #739
- [ ] https://github.com/octo-org/octo-repo/issues/740
- [ ] Add delight to the experience when all tasks are complete :tada:


Si la descripción de un elemento de la lista de tareas comienza por un paréntesis, necesitará agregar el carácter de escape \\:

`- [ ] \(Optional) Open a followup issue`

- [ ] \(Optional) Open a followup issue

Para más información, consulta [About tasklists](/es/get-started/writing-on-github/working-with-advanced-formatting/about-task-lists).



# [Usar emojis](#usar-emojis)

Puedes agregar emoji a la escritura escribiendo `:EMOJICODE:`, dos puntos seguidos del nombre del emoji.

`@octocat :+1: This PR looks great - it's ready to merge! :shipit:`

@octocat :+1: This PR looks great - it's ready to merge! :shipit:


Escriba : mostrará una lista de emojis sugeridos. La lista se filtrará a medida que escriba, por lo que una vez que encuentre el emoji que está buscando, pulse **Tab** o **Entrar** para completar el resultado resaltado.

Para obtener una lista completa de los códigos y emoji disponibles, consulta [la hoja de referencia rápida de los emoji](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md).


# [Párrafos](#parrafos)

Puedes crear un nuevo párrafo al dejar una línea en blanco entre las líneas de texto.


# [Notas al pie](#notas-al-pie)

Puedes agregar notas al pie para tu contenido si utilizas esta sintaxis de corchetes:

```text
Here is a simple footnote[^1].

A footnote can also have multiple lines[^2].

[^1]: My reference.
[^2]: To add line breaks within a footnote, prefix new lines with 2 spaces.
  This is a second line.
```
Here is a simple footnote[^1].

A footnote can also have multiple lines[^2].

[^1]: My reference.
[^2]: To add line breaks within a footnote, prefix new lines with 2 spaces.
  This is a second line.
Vete al final del artículo para ver la nota al pie

![Captura de pantalla de Markdown en la que se muestran los números de superíndice usados para indicar notas al pie, junto con saltos de línea opcionales dentro de una nota.](/assets/cb-27017/images/help/writing/footnote-rendered.png)

> [!Note]  
> La posición de una nota al pie de página en Markdown no influye en dónde se representará la nota al pie de página. Puedes escribir una nota al pie después de referenciarla y esta aún se interpretará en la parte inferior del archivo con lenguaje de marcado. Las notas al pie no se admiten en las wikis.


# [Alertas](#alertas)

Las alertas son una extensión Markdown basada en la sintaxis blockquote que puede utilizar para resaltar la información crítica. En GitHub, se muestran con colores e iconos distintivos para indicar la importancia del contenido.

Deben usarse las alertas solo cuando sean cruciales para el éxito del usuario y limitarlas a una o dos por artículo para evitar sobrecargar al lector. Además, debe evitarse colocar alertas consecutivamente. Las alertas no se pueden anidar dentro de otros elementos.

Para agregar una alerta, debe usarse una línea blockquote especial que especifique el tipo de alerta, seguida de la información de alerta en un blockquote estándar. Existen cinco tipos de alertas.

```markdown
> [!NOTE]
> Useful information that users should know, even when skimming content.

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.
```

> [!NOTE]
> Useful information that users should know, even when skimming content.

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.
Estas son las alertas representadas:



# [Ocultar el contenido con comentarios](#ocultar-el-contenido-con-comentarios)

Puedes indicarle a GitHub que oculte el contenido del Markdown representado si colocas el contenido en un comentario HTML.

```text
<!-- This content will not appear in the rendered Markdown -->
```

<!-- This content will not appear in the rendered Markdown -->

Puedes ver en el archivo .md que la linea indicada aparece en el texto y se ha omitido.


# [Ignorar formato de Markdown](#ignoranr-formato-de-markdown)

Puedes indicarle a GitHub que ignore (u omita) el formato de Markdown si usas \\ antes del carácter de Markdown.

`Let's rename \*our-new-project\* to \*our-old-project\*.`

Let's rename \*our-new-project\* to \*our-old-project\*.

Podemos observar como no se ha puesto en cursiva `our-new project` ni `our-old-project`.

Para obtener más información, consulte [Sintaxis de Markdown](https://daringfireball.net/projects/markdown/syntax#backslash) de Daring Fireball.

> [!NOTE]  
> El formato de Markdown no se omitirá en el título de un problema o de una solicitud de incorporación de cambios.

# [Tablas](#tablas)
Puede crear tablas con canalizaciones `|` y guiones `-`. Los guiones se usan para crear cada encabezado de columna, mientras que las barras verticales separan cada columna. Debes incluir una línea en blanco antes de tu tabla para que se representen correctamente.

```markdown

| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
```


| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |

Las barras verticales en cada lado de la tabla son opcionales.

Las celdas pueden variar en el ancho y no es necesario que estén perfectamente alineadas dentro de las columnas. Debe haber al menos tres guiones en cada columna de la línea de encabezamiento.

```markdown
| Command | Description |
| --- | --- |
| git status | List all new or modified files |
| git diff | Show file differences that haven't been staged |
```


| Command | Description |
| --- | --- |
| git status | List all new or modified files |
| git diff | Show file differences that haven't been staged |



Si editas fragmentos de código y tablas con frecuencia, puedes beneficiarte de habilitar una fuente de ancho fijo en todos los campos de comentarios de GitHub. Para más información, consulta [Acerca de escritura y formato en GitHub](/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/about-writing-and-formatting-on-github#enabling-fixed-width-fonts-in-the-editor).

## [Formatear el contenido dentro de tu tabla](#formatting-content-within-your-table)

Puede usar [formatos](/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax), como vínculos, bloques de código insertados y estilos de texto en la tabla:

```markdown
| Command | Description |
| --- | --- |
| `git status` | List all *new or modified* files |
| `git diff` | Show file differences that **haven't been** staged |
```

| Command | Description |
| --- | --- |
| `git status` | List all *new or modified* files |
| `git diff` | Show file differences that **haven't been** staged |


Puede alinear el texto a la izquierda, a la derecha o en el centro de una columna al incluir dos puntos `:` a la izquierda, a la derecha o a ambos lados de los guiones en la línea de encabezamiento.

```markdown
| Left-aligned | Center-aligned | Right-aligned |
| :---         |     :---:      |          ---: |
| git status   | git status     | git status    |
| git diff     | git diff       | git diff      |
```

| Left-aligned | Center-aligned | Right-aligned |
| :---         |     :---:      |          ---: |
| git status   | git status     | git status    |
| git diff     | git diff       | git diff      |



Para incluir una barra vertical `|` como contenido en su celda, utilice una `\` antes de la barra vertical:

```markdown
| Name     | Character |
| ---      | ---       |
| Backtick | `         |
| Pipe     | \|        |
```

| Name     | Character |
| ---      | ---       |
| Backtick | `         |
| Pipe     | \|        |


# [Secciones contraidas](#secciones-contraidas)
Creación de una sección contraída

Puede ocultar temporalmente las secciones de Markdown mediante la creación de una sección contraída que el lector puede elegir expandir. Por ejemplo, si quiere incluir detalles técnicos en el comentario una incidencia que puede no ser relevante o interesante para todos los lectores, puede colocar esos detalles en una sección contraída.

Cualquier Markdown dentro del bloque `<details>` se contraerá hasta que el lector haga clic en para expandir los detalles.

Dentro del bloque `<details>`, usa la etiqueta `<summary>` para que los lectores sepan lo que hay dentro. La etiqueta aparece a la derecha de .

````markdown
<details>

<summary>Tips for collapsed sections</summary>

### You can add a header

You can add text within a collapsed section.

You can add an image or a code block, too.

```ruby
   puts "Hello World"
```

</details>
````

El Markdown dentro de etiqueta `<summary>` se contraerá de forma predeterminada

Después de que un lector haga clic en , los detalles se expanden.

<details>

<summary>Tips for collapsed sections</summary>

### You can add a header

You can add text within a collapsed section.

You can add an image or a code block, too.

```ruby
   puts "Hello World"
```

</details>


Opcionalmente, para que la sección se muestre como abierta de manera predeterminada, agregue el atributo `open` a la etiqueta `<details>`:


# [Crear y resaltar bloques de código](#crear-y-resaltar-bloques-de-codigo)


> [!NOTE]
> Para preservar tu formato en una lista, asegúrate de dejar una sangría de ocho espacios en los bloques de código no delimitados.

Para mostrar las comillas simples triples en un bloque de código cercado, enciérralas en comillas simples cuádruples.

`````text
````
```
Look! You can see my backticks.
```
````
`````


````
```
Look! You can see my backticks.
```
````

## [Resaltado de sintaxis](#syntax-highlighting)

Puedes agregar un identificador opcional de idioma para habilitar el resaltado de la sintaxis en tu bloque de código cercado.

El resaltado de sintaxis cambia el color y el estilo del código fuente para facilitar la lectura.

Por ejemplo, para resaltar la sintaxis del código Ruby:

````text
```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```
````

```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```
Se mostrará el bloque de código con resaltado de sintaxis:  
Usamos [Linguist](https://github.com/github-linguist/linguist) (Lingüista) para realizar la detección de idioma y seleccionar [gramáticas de terceros](https://github.com/github-linguist/linguist/blob/main/vendor/README.md) para el resaltado de sintaxis. Puede averiguar qué palabras clave son válidas en [el archivo YAML de idiomas](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml).


# [Diagramas](#diagramas)

## [Acerca de crear diagramas](#about-creating-diagrams)

Puede crear diagramas en Markdown con cuatro sintaxis diferentes: Mermaid, geoJSON, topoJSON, y ASCII STL. La representación de diagramas está disponible en los archivos GitHub Issues, GitHub Discussions, solicitudes de incorporación de cambios, wikis y Markdown.

## [Crear diagramas de Mermaid](#creating-mermaid-diagrams)

Mermaid es una herramienta inspirada en Markdown que representa texto en diagramas. Por ejemplo, Mermaid puede representar gráficos de flujo, diagramas de secuencia, gráficos circulares y mucho más. Para obtener más información, vea la [documentación de Mermaid](https://mermaid-js.github.io/mermaid/#/).

Para crear un diagrama de Mermaid, agregue la sintaxis de Mermaid dentro de un bloque de código delimitado con el identificador de idioma `mermaid`. Para más información sobre cómo crear bloques de código, consulta [Crear y resaltar bloques de código](/es/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks).

Por ejemplo, puedes crear un gráfico de flujo especificando valores y flechas.

````text
Here is a simple flow chart:

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```
````

![Captura de pantalla de un gráfico de flujo de Sirena representado con cuatro cuadros de lavanda etiquetados como A, B, C y D. Las flechas se extienden de A a B, de B a D, de A a C y de C a D.](/assets/cb-46019/images/help/writing/mermaid-flow-chart.png)

Nota:

Es posible que observes errores si ejecutas un complemento de Mermaid de terceros al usar la sintaxis de Mermaid en GitHub.

### [Comprobación de su versión de Mermaid](#checking-your-version-of-mermaid)

Para asegurarse de que GitHub} admite la sintaxis de Mermaid, compruebe la versión de Mermaid que está actualmente en uso.

````text
```mermaid
  info
```
````


# [Creación de mapas GeoJSON y TopoJSON](#creacion-de-mapas-geojson-y-topojson)

Puedes usar la sintaxis GeoJSON o TopoJSON para crear mapas interactivos. Para crear un mapa, agrega GeoJSON o TopoJSON dentro de un bloque de código delimitado con el identificador de sintaxis `geojson` o `topojson`. Para más información, consulta [Crear y resaltar bloques de código](/es/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks).

## [Uso de GeoJSON](#using-geojson)

Por ejemplo, puedes crear un mapa especificando coordenadas.

````text
```geojson
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "id": 1,
      "properties": {
        "ID": 0
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
              [-90,35],
              [-90,30],
              [-85,30],
              [-85,35],
              [-90,35]
          ]
        ]
      }
    }
  ]
}
```
````

![Captura de pantalla de un mapa GeoJSON representado del sudeste de Estados Unidos con una superposición rectangular púrpura en partes de Alabama y Misisipi.](/assets/cb-304239/images/help/writing/fenced-geojson-rendered-map.png)

## [Uso de TopoJSON](#using-topojson)

Por ejemplo, puedes crear un mapa de TopoJSON especificando coordenadas y formas.

````text
```topojson
{
  "type": "Topology",
  "transform": {
    "scale": [0.0005000500050005, 0.00010001000100010001],
    "translate": [100, 0]
  },
  "objects": {
    "example": {
      "type": "GeometryCollection",
      "geometries": [
        {
          "type": "Point",
          "properties": {"prop0": "value0"},
          "coordinates": [4000, 5000]
        },
        {
          "type": "LineString",
          "properties": {"prop0": "value0", "prop1": 0},
          "arcs": [0]
        },
        {
          "type": "Polygon",
          "properties": {"prop0": "value0",
            "prop1": {"this": "that"}
          },
          "arcs": [[1]]
        }
      ]
    }
  },
  "arcs": [[[4000, 0], [1999, 9999], [2000, -9999], [2000, 9999]],[[0, 0], [0, 9999], [2000, 0], [0, -9999], [-2000, 0]]]
}
```
````

![Captura de pantalla de un mapa TopoJSON representado de Indonesia, Singapur y Malasia con un punto azul, una superposición rectangular púrpura y líneas azules en zigzag.](/assets/cb-434182/images/help/writing/fenced-topojson-rendered-map.png)

Para más información sobre cómo trabajar con archivos `.geojson` y `.topojson`, consulta [Trabajo con archivos que no son de código](/es/repositories/working-with-files/using-files/working-with-non-code-files#mapping-geojson-files-on-github).

## [Crear modelos STL 3D](#creating-stl-3d-models)

Puede usar la sintaxis STL ASCII directamente en Markdown para crear modelos 3D interactivos. Para mostrar un modelo, agregue la sintaxis STL ASCII dentro de un bloque de código cercado con el identificador de sintaxis `stl`. Para más información, consulta [Crear y resaltar bloques de código](/es/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks).

Por ejemplo, puede crear un modelo 3D sencillo:

````text
```stl
solid cube_corner
  facet normal 0.0 -1.0 0.0
    outer loop
      vertex 0.0 0.0 0.0
      vertex 1.0 0.0 0.0
      vertex 0.0 0.0 1.0
    endloop
  endfacet
  facet normal 0.0 0.0 -1.0
    outer loop
      vertex 0.0 0.0 0.0
      vertex 0.0 1.0 0.0
      vertex 1.0 0.0 0.0
    endloop
  endfacet
  facet normal -1.0 0.0 0.0
    outer loop
      vertex 0.0 0.0 0.0
      vertex 0.0 0.0 1.0
      vertex 0.0 1.0 0.0
    endloop
  endfacet
  facet normal 0.577 0.577 0.577
    outer loop
      vertex 1.0 0.0 0.0
      vertex 0.0 1.0 0.0
      vertex 0.0 0.0 1.0
    endloop
  endfacet
endsolid
```
````

![Captura de pantalla de un modelo 3D de una pirámide azul sobre una cuadrícula de líneas negras. Las opciones "Wireframe" (Retícula), "Surface Angle" (Ángulo de superficie) o "Solid" (Sólido) aparecen en la parte inferior.](/assets/cb-123217/images/help/writing/fenced-stl-rendered-object.png)


# [Expresiones matemáticas](#expresiones-matemáticas)

## [Acerca de la escritura de expresiones matemáticas](#about-writing-mathematical-expressions)

Para habilitar una comunicación clara de las expresiones matemáticas, GitHub admite expresiones matemáticas con formato LaTeX en Markdown. Para obtener más información, consulta [LaTeX/Expresiones matemáticas](http://en.wikibooks.org/wiki/LaTeX/Mathematics) en Wikibooks.

La funcionalidad de representación de expresiones matemáticas de GitHub usa MathJax, un motor de visualización de código abierto basado en JavaScript. MathJax admite una amplia gama de macros de LaTeX y varias extensiones de accesibilidad útiles. Para obtener más información, consulta la [documentación de MathJax](http://docs.mathjax.org/en/latest/input/tex/index.html#tex-and-latex-support) y la [documentación sobre extensiones de accesibilidad de MathJax](https://mathjax.github.io/MathJax-a11y/docs/#reader-guide).

La representación de expresiones matemáticas está disponible en los archivos GitHub Issues, GitHub Discussions, solicitudes de incorporación de cambios, wikis y Markdown.

## [Escritura de expresiones insertadas](#writing-inline-expressions)

Hay dos opciones para delimitar una expresión matemática insertada con el texto. Puedes rodear la expresión con símbolos de dólar (`$`) o iniciar la expresión con `` $` `` y terminarla con `` `$ ``. Esta última sintaxis es útil cuando la expresión que escribes contiene caracteres que se superponen con la sintaxis de Markdown. Para más información, consulta [Sintaxis de escritura y formato básicos](/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

```text
This sentence uses `$` delimiters to show math inline: $\sqrt{3x-1}+(1+x)^2$
```

![Recorte de pantalla del Markdown representado en el que se muestra una expresión matemática insertada: la raíz cuadrada de 3x menos 1 más (1 más x) al cuadrado.](/assets/cb-6685/images/help/writing/inline-math-markdown-rendering.png)

```text
This sentence uses $\` and \`$ delimiters to show math inline: $`\sqrt{3x-1}+(1+x)^2`$
```

![Recorte de pantalla del Markdown representado en el que se muestra una expresión matemática insertada con sintaxis de comillas simples: la raíz cuadrada de 3x menos 1 más (1 más x) al cuadrado.](/assets/cb-10142/images/help/writing/inline-backtick-math-markdown-rendering.png)

## [Escritura de expresiones como bloques](#writing-expressions-as-blocks)

Para agregar una expresión matemática como un bloque, empieza una línea nueva y delimita la expresión con dos símbolos de dólar (`$$`).

Sugerencia

Si estás escribiendo en un archivo .md, deberás usar un formato específico para crear un salto de línea, como finalizar la línea con una barra diagonal inversa, tal y como se muestra en el ejemplo siguiente. Para más información sobre el uso de saltos de línea en Markdown, consulta [Sintaxis de escritura y formato básicos](/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#line-breaks).

```text
**The Cauchy-Schwarz Inequality**\
$$\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)$$
```

**The Cauchy-Schwarz Inequality**\
$$\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)$$


Otra opción es usar la sintaxis de bloque de código ` ```math ` para mostrar una expresión matemática como un bloque. Con esta sintaxis, no es necesario usar los delimitadores `$$`. Lo siguiente se representará igual que antes:

````text
**The Cauchy-Schwarz Inequality**

```math
\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)
```
````

## [Escritura de signos de dólar insertados y dentro de expresiones matemáticas](#writing-dollar-signs-in-line-with-and-within-mathematical-expressions)

Para mostrar un signo de dólar como un carácter en la misma línea que una expresión matemática, debes incluir en una secuencia de escape el signo `$` que no es un delimitador para asegurarte de que la línea se representa correctamente.

*   Dentro de una expresión matemática, agrega el símbolo `\` antes del símbolo `$` explícito.
    
    ```text
    This expression uses `\$` to display a dollar sign: $`\sqrt{\$4}`$
    ```
    
    ![Captura de pantalla de Markdown representada en la que se muestra cómo una barra diagonal inversa antes de un signo de dólar muestra el signo como parte de una expresión matemática.](/assets/cb-30316/images/help/writing/dollar-sign-within-math-expression.png)
    
*   Fuera de una expresión matemática, pero en la misma línea, rodea de etiquetas "span" el símbolo `$` explícito.
    
    ```text
    To split <span>$</span>100 in half, we calculate $100/2$
    ```
    
    ![Recorte de pantalla del Markdown representado en el que se muestra cómo las etiquetas de intervalo alrededor de un signo de dólar muestran el signo como texto insertado, no como una ecuación matemática.](/assets/cb-22382/images/help/writing/dollar-sign-inline-math-expression.png)
    




# [Referencias](#referencias)

Cogido de [Documentación de github](https://docs.github.com/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
