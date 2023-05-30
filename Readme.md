# API Import CSV and Rating
> Es una API que importa un CSV y Luego esa data la inserta en la BD, para luego ser analizada.

## Tabla de contenidos
* [Plantilla CSV](#introduccion)
* [Configuracion del proyecto](#config)
* [URLs](#url)
* [Contacto](#contacto)

## Introducción <a name="introduccion"></a> 
  ### Escribe aquí:
  - Para poder utilizar el proyecto, debes descargar el siguiente archivo CSV
  - Archivo de Prueba(https://recruiting-datasets.s3.us-east-2.amazonaws.com/restaurantes.csv)


## Configuracion del Proyecto <a name="config"></a> 
  ### Escribe aquí:
  Deben ejecutar el siguiente comando en su terminal
  - git clone https://github.com/Alberbackdev/restaurant_test.git

  - Luego deben crear un entorno virtual e instalar el documento requirements.txt con el siguiente comando
 
  -> Entorno Virtual: python -m virtualenv venv 
  -> Dependencias: pip install -r requirements.txt
  
  - Debe tener postgresql instalado 
  - Ejecutar el shell psql 
  - Crear la base de datos con el siguiente comando:
  -> CREATE DATABASE crud_csv;

  - Editar en el archivo crudData/settings.py la Variable de entorno DATABASES con los siguientes datos
  -> 'NAME':'crud_csv',
  -> 'USER':'TU USUARIO DE BASE DE DATOS', 
  -> 'PASSWORD':'TU PASSWORD',
  -> 'HOST':'localhost',
  -> 'PORT':'Tu puerto de conexion', 

  Luego ejecutas las migraciones
  - python manage.py migrate

## URLs <a name="url"></a> 
- Para acceder a las Apis creadas dirijase a la siguiente url: http://127.0.0.1:8000/api/
- Para Acceder a la documentacion de la API: http://127.0.0.1:8000/redoc/
- Para Acceder al panel admin: http://127.0.0.1:8000/admin/login/?next=/admin/
- Username: alber
- Password: 1234567890

## Contacto 
- Mail: albertograterolca@gmail.com