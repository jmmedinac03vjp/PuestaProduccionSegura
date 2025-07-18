# Actividad - Análisis estático de código con Santoku
```bash
cd Android-InsecureBankv2/
qark --apk InsecureBankv2.apk
```

/home/usuario/.local/lib/python2.7/site-packages/qark/report/report.html
![](images/image1.png) 

```bash
mkdir APKDescomprimida
cp InsecureBankv2.apk APKDescomprimida/
cd APKDescomprimida/
apktool d InsecureBankv2.apk

```
![](images/image3.png)
![](images/image4.png)



```bash
gedit InsecureBankv2/AndroidManifest.xml 
```
![](images/image5.png)
```bash
androlyze -s
```


```androlize
a, d, dx = AnalyzeAPK("InsecureBankv2.apk")
show_Permissions(dx)
quit
```
![](images/image6.png)
![](images/image7.png)


```bash
cd Descargas/
java -jar bytecode-Viewer

```
- Detectar logs
![](images/image8.png)

![](images/image9.png)
- Detectar intents
![](images/image10.png)

-broadcast
![](images/image11.png)

- Comunicaciones inseguras
![](images/image12.png)

![](images/image13.png)
- Cifrado inseguro
![](images/image14.png)

-webviews 
![](images/image16.png)

-Acceso a contenidos de Content Providers
![](images/image18.png)

-Acceso a Ficheros
![](images/image17.png)
 

-Ejecución JavaScript

-Mode_world_readable
![](images/image19.png)

- Uso de Almacenamiento Externo
```bash
androlyze -s
```


```androlize
a, d, dx = AnalyzeAPK("InsecureBankv2.apk")
show_Paths(d, dx.tainted_packages.search_methods(".", "getExternalStorageDirectory", "."))
show_Paths(d, dx.tainted_packages.search_methods(".", "getExternalFilesDir", "."))

quit
```

![](images/image20.png)
![](images/image21.png)
![](images/image22.png)

- Comprobación Emulación y rooteado
![](images/image23.png)
```bash
androlyze -s
```


```androlize
a, d, dx = AnalyzeAPK("InsecureBankv2.apk")
show_Paths(d, dx.tainted_packages.search_methods(".", "getRuntime", "."))

quit
```
![](images/image24.png)

- Componente invisible en base a un recurso.

![](images/image25.png)

Buscamos string `2131165258`

![](images/image26.png)
