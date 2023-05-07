## Entrega Final Python - Django :clipboard:

##### La entrega final del curso de python de CoderHouse dictado por el prof. Franco Gabriel Di Martino, por el tutor Enzo Martin Zotti y la breve pero no menos importante participacion de porf. Norman Beltran. Esta entrega final 

#### Objetivo 
##### Desarrollar una WEB Django con patrón MVT subida a Github.

#### Consigna principal:
##### En forma individual, crearás una aplicación web estilo blog programada en Python en Django. Esta web tendrá admin, perfiles, registro, páginas y formularios.

#### Criteros de evaluación:

- Inicio: Al momento de ingresar a la app en la ruta base ‘/’
Visualizar el home del blog.
- Poder listar todas las páginas del blog, poder ver en detalle cada una, poder crear, editar o borrar páginas del blog.
- Las páginas están formadas por un título, un contenido en editor de texto avanzado (ckeditor por ejemplo), una imagen, fecha de posteo de la imagen.
- Tener una app de registro donde se puedan registrar usuarios en el route accounts/signup, un usuario está compuesto por: email - contraseña - nombre de usuario
Tener una app de login en el route accounts/login/ la cual permite loggearse con los datos de administrador o de usuario normal.
- Tener una app de perfiles en el route accounts/profile/ la cual muestra la info de nuestro usuario y permite poder modificar y/o borrar: imagen - nombre - descripción -  un link a una página web - email y contraseña
- Contar con un admin en route admin/ donde se puedan manejar las apps y los datos en las apps.
- Tener una app de mensajería en el route messages/ para que los perfiles se puedan contactar entre sí.


#### Formato  

##### Link al repositorio de GitHub con el nombre “Entrega_Final+Apellido”.

#### Pasos :gear:

 ##### 1. Para la confección de este entregable se realizo un modelo de la plantilla a usar en papel para luego codificarla con Bootstrap y Css.

 ##### 2. Se uso el editor de codigo Visual Studio Code donde se trabajo con la extension Python que podemos encontrar en la galeria de extensiones.

 ##### 3. Tambien se instalo Django en su ultima version para poder llevar a cabo el proyecto con este Framework.

 ##### 4. Se inicio un nuevo proyecto en django creando una carpeta, la cual vamos a abrir desde Visual Studio Code y en la consola escribimos el comando django-admin startproject + nombre de nuestro proyecto


 ##### 5. Luego tipeamos" python manage.py migrate" y veificamos que todo este en orden con el comando "python manage.py runserver" al correr django veremos una pagina de inicio proporcionada por el framework.

##### 6. Funcionando django vamos a crear nuestro primer archivo "views.py",  Vamos a nuestro archivo views.py, e importamos los elementos de un Response: 
from django.http import HttpResponse

##### 7. Con todos estos pasos podemos coemnzar a trabajar en nuestra pagina.
 ##### 8. Otro paso para la creacion de es Cat Cafe fue crear la app AppCoder y AppCoderSocial donde se alojaron tantos los template como toda la informacion.

 ##### 9. Para este blog se crearon una pagina de inicio y 3 formularios para el correcto manejo de la informacion que se aloja en SQL lite.

###### video [video Cat_Cafe](https://drive.google.com/file/d/1-iTr0Txl_ixZFQCBOkG11DfQpWJL_vbP/view?usp=sharing) 
###### Todo esto y mas podras ver en mi [GitHub](https://github.com/Danisole/) 


##### Fotos

![Inicio](./proyecto_py/AppCoder/static/AppCoder/assets/Captura%20de%20pantalla%20(31).png)

![Vistas](./proyecto_py/AppCoder/static/AppCoder/assets/Captura%20de%20pantalla%20(32).png)


