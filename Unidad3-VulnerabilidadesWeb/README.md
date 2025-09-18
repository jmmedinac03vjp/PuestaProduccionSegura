# Unidad 3 - Detección y corrección de vulnerabilidades de aplicaciones web

**Índice**

[Objetivos](#objetivos)

[Resultados de aprendizaje y Criterios de Evaluación](#resultados-de-aprendizaje-y-criterios-de-evaluación)

[Contenidos Teóricos](#contenidos-teóricos)

[Actividades](#actividades)

[Línea de vida](#línea-de-vida)

[Recursos y contenidos extra](#recursos-y-contenidos-extra)

---
# Objetivos

---

# Resultados de aprendizaje y Criterios de Evaluación

En esta unidad se aplica el RA3: Detecta y corrige vulnerabilidades de aplicaciones web analizando su código fuente y configurando servidores web.

**Criterios de evaluación:**

a)	Se han validado las entradas de los usuarios.

b)	Se han detectado riesgos de inyección tanto en el servidor como en el cliente.

c)	Se ha gestionado correctamente la sesión del usuario durante el uso de la aplicación.

d)	Se ha hecho uso de roles para el control de acceso.

e)	Se han utilizado algoritmos criptográficos seguros para almacenar las contraseñas de usuario.

f)	Se han configurado servidores web para reducir el riesgo de sufrir ataques conocidos.

g)	Se han incorporado medidas para evitar los ataques a contraseñas, envío masivo de mensajes o registros de usuarios a través de programas automáticos (bots).


---
# Contenidos Teóricos

- Desarrollo seguro de aplicaciones web.
- Listas públicas de vulnerabilidades de aplicaciones web. OWASP Top Ten.
- Entrada basada en formularios. Inyección. Validación de la entrada.
- Estándares de autenticación y autorización.
- Robo de sesión.
- Vulnerabilidades web.
- Almacenamiento seguro de contraseñas.
- Contramedidas: HSTS, CSP, CAPTCHAs, entre otros.
- Seguridad de portales y aplicativos web. Soluciones WAF(Web Application Firewall).


---
# Actividades

- [Actividad-CreacionEntornosPrueba](./Actividad-CreacionEntornoPrueba/README.md)
- [Actividad-DeteccionEquiposPuertos](Actividad-DeteccionEquiposPuertos/README.md)
- [Actividad-InyeccionSQL](Actividad-InyeccionSQL/README.md)
- [Actividad-CrossSiteScripting-XSS](Actividad-CrossSiteScripting-XSS/README.md)
- [Actividad-RemoteCodeExecution-RCE](Actividad-RemoteCodeExecution-RCE/README.md)
- [Actividad-LocalFileInclusion-LFI](Actividad-LocalFileInclusion-LFI/README.md)
- [Actividad-RemoteFileInclusion-RFI](Actividad-RemoteFileInclusion-RFI/README.md)
- [Actividad-DeserializacionInsegura](Actividad-DeserializacionInsegura/README.md)
- [Actividad-GestionInseguraSesiones](Actividad-GestionInseguraSesiones/README.md)
- [Actividad-CrossSiteRequestForgery-CSRF](Actividad-CrossSiteRequestForgery-CSRF/README.md)
- [Actividad-BrokenAuthentication](Actividad-BrokenAuthentication/README.md)
- [Actividad-LogingMonitoring](Actividad-LogingMonitoring/README.md)
- [Actividad-ConfiguracionSeguraTLS](Actividad-ConfiguracionSeguraTLS/README.md)
- [Actividad-ContentSecurityPoliceCSP](Actividad-ContentSecurityPoliceCSP/README.md)
- [Actividad-HSTS](Actividad-HSTS/README.md)
- [](/README.md)
- [Actividad-AnalisisEstaticoCodigoSAST](Actividad-AnalisisEstaticoCodigoSAST/README.md)
- [](/README.md)
- [Actividad-AnalisisEstaticoSantoku](Actividad-AnalisisEstaticoSantoku/README.md)
- [Actividad-AnalisisSeguridadDinamicoDAST](Actividad-AnalisisSeguridadDinamicoDAST/README.md)
- [Actividad-EscaneoOWASPZAP](Actividad-EscaneoOWASPZAP/README.md)
- [](/README.md)
- [](/README.md)
- [Actividad-HardeningSevidorApache-HTTPS-HSTS-WAF](Actividad-HardeningSevidorApache-HTTPS-HSTS-WAF/README.md)
- [Actividad-AnalisisDinamicoMobSFGenymotion](Actividad-AnalisisDinamicoMobSFGenymotion/README.md)
- [](/README.md)


---

# Línea de vida
- En esta unidad vamos a ver las principales vulnerabilidades web.
- Comenzamos haciendo una introducción en la presentación [Detección y corrección de vulnerabilidades en Aplicaciones Web](./ContenidosTeoricos/PPSUnidad3-DeteccionCorrecionVulnerabilidadesWeb.pdf)
- Luego empezamos viendo las vulnerabilidades de datos de entrada con las de Inyección de codigo, desde la presentación [Detección y corrección de vulnerabilidades en aplicaciones web: Inyección de código](./ContenidosTeoricos/PPSUnidad3-VulnerabilidadesInyeccionCodigo.pdf).
- Tenemos las siguientes actividades relacionadas con las vulnerabilidades de datos de entrada:
    - [Actividad-DeteccionEquiposPuertos](Actividad-DeteccionEquiposPuertos/README.md)
    - [Actividad-InyeccionSQL](Actividad-InyeccionSQL/README.md)
    - [Actividad-CrossSiteScripting-XSS](Actividad-CrossSiteScripting-XSS/README.md)
    - [Actividad-RemoteCodeExecution-RCE](Actividad-RemoteCodeExecution-RCE/README.md)

- Seguimos con los contenidos teóricos con la presentación [Otros tipos de vulnerabilidades de entrada](./ContenidosTeoricos/PPSUnidad3-OtrasVulnerabilidadesEntrada.pdf) en las que vemos ataques como XXE, Deserialización insegura, y Inclusión de Ficheros.
- Algunas de las actividades en las que veremos esos ataques son:
    - [Actividad-LocalFileInclusion-LFI](Actividad-LocalFileInclusion-LFI/README.md)
    - [Actividad-RemoteFileInclusion-RFI](Actividad-RemoteFileInclusion-RFI/README.md)
    - [Actividad-DeserializacionInsegura](Actividad-DeserializacionInsegura/README.md)
    - [Actividad-CrossSiteRequestForgery-CSRF](Actividad-CrossSiteRequestForgery-CSRF/README.md)

- Veremos las vulnerabilidades web relacionadas con la autenticación y autorización y la gestión de sesión, junto con el almacenamiento seguro de contraseñas desde la presentación [Autenticación y Gestión de sesiones](./ContenidosTeoricos/PPSUnidad3-AutenticacionGestionSesiones.pdf)
- Algunas de las actividades relacionadas con esta categoría son:

    - [Actividad-GestionInseguraSesiones](Actividad-GestionInseguraSesiones/README.md)
    - [Actividad-BrokenAuthentication](Actividad-BrokenAuthentication/README.md)
- El siguiente conjunto de vulnerabilidades que veremos son las que tienen que ver con la __protección de datos sensibles y control de acceso__. En la presentación [Protección de datos sensibles y control de acceso](./ContenidosTeoricos/PPSUnidad3-ProteccionDatosSensiblesControlAcceso.pdf) podremos ver cómo asegurar los datos en transmisión y almacenamiento mediante encriptación (Almacenamaiento seguro de contraseñas) y el protocolo TLS además de diferentes contramedidas: HSTS, CSP, CAPTCHA, etc... y también veremos los diferentes modelos de control de acceso que podemos implementar en las aplicaciones.
    - [Actividad-ConfiguracionSeguraTLS](Actividad-ConfiguracionSeguraTLS/README.md)
    - [Actividad-HSTS](Actividad-HSTS/README.md)
    - [Actividad-ContentSecurityPoliceCSP](Actividad-ContentSecurityPoliceCSP/README.md)

- Para finalizar los apartados relacionadas con los diferentes conjuntos de vulnerabilidades web, a traves de la [presentación de Errores en la configuración de seguridad y Componentes vulnerables y desactualizados](./ContenidosTeoricos/PPSUnidad3-ErroresSeguridadComponentesVulnerables.pdf) veremos las vulnerabilidades que tienen que ver con Configuración defectuosa , fallos en la Monitorización y los logs de segurida y Componentes vulnerables y desactualizados. Además veremos cómo implementar un cortafuegos a nivel de aplicación: WAF.
- Podemos ver estos conceptos estudiados en las siguientes actividades.
    - [Actividad-LogingMonitoring](Actividad-LogingMonitoring/README.md) 
    - [Actividad-HardeningSevidorApache-HTTPS-HSTS-WAF](Actividad-HardeningSevidorApache-HTTPS-HSTS-WAF/README.md)

- Finalizamos la unidad conociendo herramientas con las que vamos a poder localizar las vulnerabilidades que hemos conocido durante la unidad. Para ello utilizamos la presentación [Herramientas de detección de vulnerabilidades](./ContenidosTeoricos/PPSUnidad3-HerramientasDeteccionVulnerabilidades.pdf)
- Tenemos algunas actividades donde veremos como utilizar herramientas de detección de vulnerabilidades de diferentes tipos:
    - [Actividad-AnalisisEstaticoCodigoSAST](Actividad-AnalisisEstaticoCodigoSAST/README.md)
    - [Actividad-AnalisisEstaticoSantoku](Actividad-AnalisisEstaticoSantoku/README.md)
    - [Actividad-AnalisisSeguridadDinamicoDAST](Actividad-AnalisisSeguridadDinamicoDAST/README.md)
    - [Actividad-EscaneoOWASPZAP](Actividad-EscaneoOWASPZAP/README.md)
    - [Actividad-AnalisisDinamicoMobSFGenymotion](Actividad-AnalisisDinamicoMobSFGenymotion/README.md)

---

# Recursos y contenidos extra
---
