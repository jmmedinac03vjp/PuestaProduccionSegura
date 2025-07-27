## [Encabezados](#headings)

Para crear un encabezado, agrega entre uno y seis símbolos # antes del encabezado del texto. El número de # que utilices determinará el nivel jerárquico y el tamaño tipográfico del encabezado.

```markdown
# A first-level heading
## A second-level heading
### A third-level heading
```
# A first-level heading
## A second-level heading
### A third-level heading


Al usar dos o más encabezados, GitHub genera automáticamente una tabla de contenido a la que puede acceder haciendo clic en dentro del encabezado del archivo. Todos los títulos de encabezado aparecen en la tabla de contenido, y puede hacer clic en un título para ir a la sección seleccionada.

![Recorte de pantalla de un archivo LÉAME con el menú desplegable de la tabla de contenido expuesto. El icono de la tabla de contenido aparece en naranja oscuro.](/assets/cb-69181/images/help/repository/headings-toc.png)

## [Estilos de texto](#styling-text)

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

## [Entrecomillado de texto](#quoting-text)

Puede entrecomillar texto con \>.

```markdown
Text that is not a quote

> Text that is a quote
```

Text that is not a quote

> Text that is a quote

Al texto entre comillas se le aplica sangría con una línea vertical en la izquierda y se muestra mediante texto en color gris.

!

>Nota:

Al visualizar una conversación, puedes citar automáticamente el texto en un comentario si lo resaltas y escribes R. Para citar un comentario completo, haz clic en y, a continuación, en **Citar respuesta**. Para obtener más información acerca de los métodos abreviados de teclado, consulte [Accesos directos del teclado](/es/get-started/accessibility/keyboard-shortcuts).

## [Código de cita](#quoting-code)

Puedes indicar un código o un comando dentro de un enunciado con comillas invertidas. El texto dentro de las comillas invertidas no será formateado. También puedes presionar el método abreviado de teclado Comando+E (Mac) o Ctrl+E (Windows o Linux) para insertar las comillas invertidas de bloque de código en una línea de Markdown.

```markdown
Use `git status` to list all new or modified files that haven't yet been committed.
```

![Recorte de pantalla del Markdown de GitHub representado en el que se muestra que los caracteres rodeados por acentos graves se muestran en una fuente de ancho fijo, resaltada en gris claro.](/assets/cb-24556/images/help/writing/inline-code-rendered.png)

Para formatear código o texto en su propio bloque distintivo, usa comillas invertidas triples.

````markdown
Some basic Git commands are:
```
git status
git add
git commit
```
````

![Recorte de pantalla del Markdown de GitHub representado, en el que se muestra un bloque de código simple sin resaltado de sintaxis.](/assets/cb-34231/images/help/writing/code-block-rendered.png)

Para más información, consulta [Crear y resaltar bloques de código](/es/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks).

Si editas fragmentos de código y tablas con frecuencia, puedes beneficiarte de habilitar una fuente de ancho fijo en todos los campos de comentarios de GitHub. Para más información, consulta [Acerca de escritura y formato en GitHub](/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/about-writing-and-formatting-on-github#enabling-fixed-width-fonts-in-the-editor).

## [Modelos de color compatibles](#supported-color-models)

En los problemas, las solicitudes de incorporación de cambios y los debates, puedes llamar a los colores dentro de una oración mediante comillas invertidas. Un modelo de color compatible dentro de las comillas invertidas mostrará una visualización del color.

```markdown
The background color is `#ffffff` for light mode and `#000000` for dark mode.
```

![Recorte de pantalla del Markdown de GitHub, en el que se muestra cómo los valores HEX dentro de los acentos graves crean pequeños círculos de color, primero blancos y luego negros.](/assets/cb-11643/images/help/writing/supported-color-models-rendered.png)

Estos son los modelos de color admitidos actualmente.

| Color | Sintaxis | Ejemplo | Resultados |
| --- | --- | --- | --- |
| HEX | `` `#RRGGBB` `` | `` `#0969DA` `` | ![Captura de pantalla de GitHub Markdown en la que se muestra cómo aparece el valor HEX #0969DA con un círculo azul.](/assets/cb-1558/images/help/writing/supported-color-models-hex-rendered.png) |
| RGB | `` `rgb(R,G,B)` `` | `` `rgb(9, 105, 218)` `` | ![Captura de pantalla de GitHub Markdown en la que se muestra cómo aparece el valor RGB 9, 105, 218 con un círculo azul.](/assets/cb-1962/images/help/writing/supported-color-models-rgb-rendered.png) |
| HSL | `` `hsl(H,S,L)` `` | `` `hsl(212, 92%, 45%)` `` | ![Captura de pantalla de GitHub Markdown en la que se muestra cómo aparece el valor de HSL 212, 92 %, 45 % con un círculo azul.](/assets/cb-2066/images/help/writing/supported-color-models-hsl-rendered.png) |

Nota:

*   Un modelo de color admitido no puede tener espacios iniciales o finales dentro de las comillas invertidas.
*   La visualización del color solo se admite en problemas, solicitudes de incorporación de cambios y debates.

## [Vínculos](#links)

Puede crear un vínculo en línea escribiendo su texto entre corchetes `[ ]` y escribiendo la URL entre paréntesis `( )`. También puede usar el método abreviado de teclado Command+K para crear un vínculo. Cuando haya seleccionado texto, puede pegar una dirección URL del Portapapeles para crear automáticamente un vínculo a partir de la selección.

También puedes crear un hipervínculo de Markdown resaltando el texto y usando el método abreviado de teclado Comando+V. Si quieres reemplazar el texto por el vínculo, usa el método abreviado de teclado Comando+Mayús+V.

`This site was built using [GitHub Pages](https://pages.github.com/).`

![Captura de pantalla de GitHub Markdown en la que se muestra cómo el texto entre corchetes, "GitHub Pages", aparece como un hipervínculo azul.](/assets/cb-8312/images/help/writing/link-rendered.png)

Nota:

GitHub crea vínculos automáticamente cuando se escriben direcciones URL válidas en un comentario. Para más información, consulta [Referencias y direcciones URL autovinculadas](/es/get-started/writing-on-github/working-with-advanced-formatting/autolinked-references-and-urls).

## [Enlaces de sección](#section-links)

Puede vincular directamente a cualquier sección que tenga un encabezado. Para ver el delimitador generado automáticamente en un archivo representado, mantenga el puntero sobre el encabezado de sección para exponer el icono de y haga clic en el icono para mostrar el delimitador en el explorador.

![Captura de pantalla de un archivo README de un repositorio. A la izquierda de un encabezado de sección, se destaca un icono de vínculo en naranja oscuro.](/assets/cb-55933/images/help/repository/readme-links.png)

Si necesitas determinar el ancla de un encabezado en un archivo que estás editando, puede usar las siguientes reglas básicas:

*   Las letras se convierten a minúsculas.
*   Los espacios se reemplazan por guiones (`-`). Se quitan cualquier otro espacio en blanco o caracteres de puntuación.
*   Se quitan los espacios en blanco iniciales y finales.
*   Se quita el formato de marcado, dejando solo el contenido (por ejemplo, `_italics_` se convierte en `italics`).
*   Si el ancla generada automáticamente para un encabezado es idéntico a una ancla anterior en el mismo documento, se genera un identificador único anexando un guión y un entero de incremento automático.

Para obtener información más detallada sobre los requisitos de fragmentos del identificador URI, consulte [RFC 3986: Identificador uniforme de recursos (URI): Sintaxis genérica, sección 3.5](https://www.rfc-editor.org/rfc/rfc3986#section-3.5).

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

Nota:

Si edita un encabezado o cambia el orden de los encabezados con anclas "idénticas", también deberá actualizar los vínculos a esos encabezados, ya que las anclas cambiarán.

## [Vínculos relativos](#relative-links)

Puedes definir enlaces relativos y rutas de imagen en los archivos representados para ayudar a que los lectores naveguen hasta otros archivos de tu repositorio.

Un enlace relativo es un enlace que es relativo al archivo actual. Por ejemplo, si tiene un archivo Léame en la raíz del repositorio y tiene otro archivo en _docs/CONTRIBUTING.md_, el vínculo relativo a _CONTRIBUTING.md_ en el archivo Léame podría tener este aspecto:

```text
[Contribution guidelines for this project](docs/CONTRIBUTING.md)
```

GitHub transformará de manera automática el enlace relativo o la ruta de imagen en cualquier rama en la que te encuentres actualmente, de modo que el enlace o ruta siempre funcione. La ruta de acceso del vínculo será relativa al archivo actual. Los vínculos que comienzan por `/` serán relativos a la raíz del repositorio. Puede usar todos los operandos de vínculo relativos, como `./` y `../`.

El texto del vínculo debe estar en una sola línea. El ejemplo siguiente no funcionará.

```markdown
[Contribution
guidelines for this project](docs/CONTRIBUTING.md)
```

Los enlaces relativos son más sencillos para los usuarios que clonan tu repositorio. Puede que los enlaces absolutos no funcionen en los clones de tu repositorio. Recomendamos usar enlaces relativos para consultar los archivos dentro de tu repositorio.

## [Anclas personalizadas](#custom-anchors)

Puede usar etiquetas de anclaje HTML estándar (`<a name="unique-anchor-name"></a>`) para crear puntos de anclaje de navegación para cualquier ubicación del documento. Para evitar referencias ambiguas, use un esquema de nomenclatura único para etiquetas de anclaje, como agregar un prefijo al valor de atributo `name`.

Nota:

Las anclas personalizadas no se incluirán en el esquema o tabla de contenido del documento.

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

Sugerencia

Las anclas personalizados no se tienen en cuenta por el comportamiento automático de nomenclatura y numeración de vínculos de encabezado automático.

## [Saltos de línea](#line-breaks)

Si está escribiendo en problemas, en solicitudes de extracción o en discusiones de un repositorio, GitHub generará un salto de línea automáticamente:

```markdown
This example
Will span two lines
```

Sin embargo, si está escribiendo en un archivo .md, el ejemplo anterior se representaría en una línea sin salto. Para crear un salto de línea en un archivo .md, deberá incluir uno de los elementos siguientes:

*   Incluya dos espacios al final de la primera línea.
    
    This example  
    Will span two lines
    
*   Incluya una barra diagonal inversa al final de la primera línea.
    
    ```markdown
    This example\
    Will span two lines
    ```
    
*   Incluya una etiqueta de salto de una sola línea HTML al final de la primera línea.
    
    ```markdown
    This example<br/>
    Will span two lines
    ```
    

Si deja una línea en blanco entre dos líneas, tanto los archivos .md como Markdown en problemas, en solicitudes de extracción y en discusiones mostrarán las dos líneas separadas por la línea en blanco:

```markdown
This example

Will have a blank line separating both lines
```

## [Imágenes](#images)

Puede mostrar una imagen agregando ! y ajustar el texto alternativo en `[ ]`. El texto alternativo es un texto corto equivalente a la información de la imagen. Luego, escribe el vínculo de la imagen entre paréntesis `()`.

`![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](https://myoctocat.com/assets/images/base-octocat.svg)`

![Captura de pantalla de un comentario en un problema de GitHub que muestra una imagen, agregada en Markdown, de un Octocat sonriendo y levantando un tentáculo.](/assets/cb-39744/images/help/writing/image-rendered.png)

GitHub admite la inserción de imágenes en incidencias, solicitudes de cambios, debates, comentarios y archivos `.md`. Puedes mostrar una imagen desde tu repositorio, agregar un enlace a una imagen en línea o cargar una imagen. Para obtener más información, consulte [Carga de recursos](#uploading-assets).

Nota:

Cuando quieras mostrar una imagen incluida en el repositorio, usa vínculos relativos en vez de absolutos.

Aquí tienes algunos ejemplos para utilizar enlaces relativos para mostrar una imagen.

| Context | Enlace Relativo |
| --- | --- |
| En un archivo `.md` de la misma rama | `/assets/images/electrocat.png` |
| En un archivo `.md` de otra rama | `/../main/assets/images/electrocat.png` |
| En propuestas, solicitudes de cambio y comentarios del repositorio | `../blob/main/assets/images/electrocat.png?raw=true` |
| En un archivo `.md` de otro repositorio | `/../../../../github/docs/blob/main/assets/images/electrocat.png` |
| En propuestas, solicitudes de cambios y comentarios de otro repositorio | `../../../github/docs/blob/main/assets/images/electrocat.png?raw=true` |

Nota:

Los últimos dos vínculos relativos de la tabla anterior funcionarán únicamente para las imágenes de repositorios privados si el lector tiene (como mínimo) acceso de lectura.

Para obtener más información, consulte [Vínculos relativos](#relative-links).

### [Elemento de imagen](#the-picture-element)

Se admite el elemento HTML `<picture>`.

## [Listas](#lists)

Puedes crear una lista sin ordenar. Para ello, coloca \-, \* o + antes de una o más líneas de texto.

```markdown
- George Washington
* John Adams
+ Thomas Jefferson
```

![Captura de pantalla de GitHub Markdown en la que se muestra una lista con viñetas de los nombres de los tres primeros presidentes de Estados Unidos.](/assets/cb-7925/images/help/writing/unordered-list-rendered.png)

Para ordenar tu lista, antecede cada línea con un número.

```markdown
1. James Madison
2. James Monroe
3. John Quincy Adams
```

![Captura de pantalla de GitHub Markdown en la que se muestra una lista numerada de los nombres de los presidentes cuarto, quinto y sexto de Estados Unidos.](/assets/cb-8162/images/help/writing/ordered-list-rendered.png)

### [Listas anidadas](#nested-lists)

Puedes crear una lista anidada al dejar sangría en uno o más elementos de la lista debajo de otro elemento.

Para crear una lista anidada mediante el editor web en GitHub o un editor de texto que use una fuente monoespaciada, como [Visual Studio Code](https://code.visualstudio.com/), puedes alinear la lista visualmente. Escribe los caracteres con espacio frente al elemento de la lista anidada hasta que el carácter del marcador de lista (\- o \*) se encuentre directamente debajo del primer carácter del texto en el elemento que se encuentra debajo.

```markdown
1. First list item
   - First nested list item
     - Second nested list item
```

Nota:

En el editor web, puedes aplicar o desaplicar sangría en una o varias líneas de texto si resaltas primero las líneas deseadas y, a continuación, usas Tab o mayús+Tab respectivamente.

![Recorte de pantalla del Markdown en Visual Studio Code, en el que se muestra la sangría de líneas numeradas anidadas y viñetas.](/assets/cb-7202/images/help/writing/nested-list-alignment.png)

![Recorte de pantalla del Markdown de GitHub representado, en el que se muestra un elemento numerado seguido de viñetas anidadas en dos niveles diferentes de anidamiento.](/assets/cb-7206/images/help/writing/nested-list-example-1.png)

Para crear una lista anidada en el editor de comentarios de GitHub, que no usa una fuente monoespaciada, puedes observar el elemento de lista inmediatamente anterior a la lista anidada y contar el número de caracteres que aparecen antes del contenido del elemento. Luego escribe ese número de caracteres de espacio frente al elemento de la lista anidada.

En este ejemplo, podría agregar un elemento de lista anidada bajo el elemento de lista `100. First list item` mediante la aplicación de sangría de mínimo cinco espacios en el elemento de lista anidada, ya que hay cinco caracteres (`100.` ) antes de `First list item`.

```markdown
100. First list item
     - First nested list item
```

![Recorte de pantalla del Markdown de GitHub representado, en el que se muestra un elemento de lista precedido por el número 100 seguido de un elemento con viñetas anidado un nivel a la derecha.](/assets/cb-4906/images/help/writing/nested-list-example-3.png)

Puedes crear múltiples niveles de listas anidadas mediante el mismo método. Por ejemplo, dado que el primer elemento de lista anidada tiene siete caracteres (`␣␣␣␣␣-␣`) antes del contenido `First nested list item` de la lista anidada, tendrás que aplicar sangría en el segundo elemento de lista anidada con al menos dos caracteres más (mínimo 9 espacios).

```markdown
100. First list item
     - First nested list item
       - Second nested list item
```

![Recorte de pantalla del Markdown de GitHub representado, en el que se muestra un elemento numerado precedido por el número 100 seguido por viñetas en dos niveles de anidamiento distintos.](/assets/cb-7734/images/help/writing/nested-list-example-2.png)

Para obtener más ejemplos, consulte las [especificaciones de GitHub Flavored Markdwon](https://github.github.com/gfm/#example-265).

## [Listas de tareas](#task-lists)

Para crear una lista de tareas, debe añadir como prefijo un guion y espacio, seguido de `[ ]` a los elementos de la lista. Para marcar una tarea como completada, use `[x]`.

```markdown
- [x] #739
- [ ] https://github.com/octo-org/octo-repo/issues/740
- [ ] Add delight to the experience when all tasks are complete :tada:
```

![Captura de pantalla que muestra la versión representada de Markdown. Las referencias a problemas se representan como títulos del problema.](/assets/cb-64626/images/help/writing/task-list-rendered-simple.png)

Si la descripción de un elemento de la lista de tareas comienza por un paréntesis, necesitará agregar el carácter de escape \\:

`- [ ] \(Optional) Open a followup issue`

Para más información, consulta [About tasklists](/es/get-started/writing-on-github/working-with-advanced-formatting/about-task-lists).

## [Mencionar personas y equipos](#mentioning-people-and-teams)

Puedes mencionar a una persona o [equipo](/es/organizations/organizing-members-into-teams) en GitHub si escribes @ junto con su nombre de usuario o equipo. Esto activará una notificación y llamará su atención hacia la conversación. Las personas también recibirán una notificación si editas un comentario para mencionar su nombre de usuario o el nombre del equipo. Para obtener más información sobre las notificaciones, consulta [Acerca de las notificaciones](/es/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/about-notifications).

Nota:

Solo se notificará a un usuario acerca de una mención si este tiene acceso de lectura al repositorio y, si el repositorio pertenece a una organización, el usuario es miembro de la organización.

`@github/support What do you think about these updates?`

![Captura de pantalla de GitHub Markdown en la que se muestra cómo la mención del equipo "@github/support" se representa como texto en negrita sobre el que se puede hacer clic.](/assets/cb-6949/images/help/writing/mention-rendered.png)

Cuando mencionas a un equipo padre, los miembros de los equipos hijo también reciben notificaciones, simplificando la comunicación con múltiples grupos de personas. Para más información, consulta [Acerca de los equipos](/es/organizations/organizing-members-into-teams/about-teams).

Si escribe un símbolo @, aparecerá una lista de personas o equipos en el proyecto. La lista filtra a medida que escribes, por lo que una vez que escribes el nombre de la persona o del equipo que estás buscando, puedes usar las teclas de flecha para seleccionarlos y presionar cada pestaña para ingresar para completar el nombre. En el caso de los equipos, escriba @organization/team-name y todos los miembros de ese equipo se suscribirán a la conversación.

Los resultados autocompletados se restringen a los colaboradores del repositorio y a otros participantes en el hilo.

## [Hacer referencia a propuestas y solicitudes de extracción](#referencing-issues-and-pull-requests)

Puede mencionar una lista de las incidencias y solicitudes de incorporación de cambios dentro del repositorio escribiendo #. Escribe el número o el título de la propuesta o la solicitud de extracción para filtrar la lista, y luego presiona cada pestaña o ingresa para completar el resultado resaltado.

Para más información, consulta [Referencias y direcciones URL autovinculadas](/es/get-started/writing-on-github/working-with-advanced-formatting/autolinked-references-and-urls).

## [Hacer referencia a recursos externos](#referencing-external-resources)

Si se configuran las referencias autovinculadas personalizadas para un repositorio, entonces las referencias a recursos externos, como un informe de problemas de JIRA o un ticket de Zendesk, se convertirán en vínculos acortados. Para saber qué autovínculos se encuentran disponibles en tu repositorio, contacta a alguien con permisos administrativos sobre el mismo. Para más información, consulta [Configurar enlaces automáticos para referenciar recursos externos](/es/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/configuring-autolinks-to-reference-external-resources).

## [Cargar activos](#uploading-assets)

Puedes cargar activos como imágenes si las arrastras y sueltas, las seleccionas de un buscador de archivos o si las pegas. Puede cargar recursos en las incidencias, solicitudes de incorporación de cambios, comentarios y archivos `.md` en el repositorio.

## [Usar emojis](#using-emojis)

Puedes agregar emoji a la escritura escribiendo `:EMOJICODE:`, dos puntos seguidos del nombre del emoji.

`@octocat :+1: This PR looks great - it's ready to merge! :shipit:`

![Captura de pantalla de GitHub Markdown que muestra cómo los códigos emoji para +1 y shipit se muestran visualmente como emoji.](/assets/cb-17228/images/help/writing/emoji-rendered.png)

Escriba : mostrará una lista de emojis sugeridos. La lista se filtrará a medida que escriba, por lo que una vez que encuentre el emoji que está buscando, pulse **Tab** o **Entrar** para completar el resultado resaltado.

Para obtener una lista completa de los códigos y emoji disponibles, consulta [la hoja de referencia rápida de los emoji](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md).

## [Párrafos](#paragraphs)

Puedes crear un nuevo párrafo al dejar una línea en blanco entre las líneas de texto.

## [Notas al pie](#footnotes)

Puedes agregar notas al pie para tu contenido si utilizas esta sintaxis de corchetes:

```text
Here is a simple footnote[^1].

A footnote can also have multiple lines[^2].

[^1]: My reference.
[^2]: To add line breaks within a footnote, prefix new lines with 2 spaces.
  This is a second line.
```

La nota al pie se verá así:

![Captura de pantalla de Markdown en la que se muestran los números de superíndice usados para indicar notas al pie, junto con saltos de línea opcionales dentro de una nota.](/assets/cb-27017/images/help/writing/footnote-rendered.png)

Nota:

La posición de una nota al pie de página en Markdown no influye en dónde se representará la nota al pie de página. Puedes escribir una nota al pie después de referenciarla y esta aún se interpretará en la parte inferior del archivo con lenguaje de marcado. Las notas al pie no se admiten en las wikis.

## [Alertas](#alerts)

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

Estas son las alertas representadas:

![Captura de pantalla de las alertas de Markdown representadas en las que se muestra cómo se representan Nota, Recomendación, Importante, Advertencia y Precaución con diferentes iconos y texto en color.](/assets/cb-24696/images/help/writing/alerts-rendered.png)

## [Ocultar el contenido con comentarios](#hiding-content-with-comments)

Puedes indicarle a GitHub que oculte el contenido del Markdown representado si colocas el contenido en un comentario HTML.

```text
<!-- This content will not appear in the rendered Markdown -->
```

## [Ignorar formato de Markdown](#ignoring-markdown-formatting)

Puedes indicarle a GitHub que ignore (u omita) el formato de Markdown si usas \\ antes del carácter de Markdown.

`Let's rename \*our-new-project\* to \*our-old-project\*.`

![Captura de pantalla de GitHub Markdown que muestra cómo las barras diagonales inversas impiden la conversión de asteriscos en cursiva.](/assets/cb-5440/images/help/writing/escaped-character-rendered.png)

Para obtener más información, consulte [Sintaxis de Markdown](https://daringfireball.net/projects/markdown/syntax#backslash) de Daring Fireball.

Nota:

El formato de Markdown no se omitirá en el título de un problema o de una solicitud de incorporación de cambios.

## [Inhabilitar la representación del lenguaje de marcado](#disabling-markdown-rendering)

Cuando ves un archivo de lenguaje de marcado, puedes hacer clic en **Código** en la parte superior de este para inhabilitar la representación de lenguaje de marcado y ver en su lugar el código fuente del archivo.

![Captura de pantalla de un archivo Markdown en un repositorio que muestra las opciones para interactuar con el archivo. Un botón, con la etiqueta "Código", está resaltado en naranja oscuro.](/assets/cb-11496/images/help/writing/display-markdown-as-source-global-nav-update.png)

El inhabilitar la interpretación de lenguaje de marcado te permite utilizar las características de vista de código fuente, tales como el enlazado de líneas, el cual no es posible cuando se está viendo un archivo interpretado en lenguaje de marcado.

## [Información adicional](#further-reading)

*   [Especificación de GitHub Flavored Markdown](https://github.github.com/gfm/)
*   [Acerca de escritura y formato en GitHub](/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/about-writing-and-formatting-on-github)
*   [Trabajar con formato avanzado](/es/get-started/writing-on-github/working-with-advanced-formatting)
*   [Inicio rápido para escribir en GitHub](/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github)