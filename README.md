# Proyecto Urban Routes con Selenium 
## QA-project-Urban-Routes-es
#### _Aldana Guzmán Aylín, grupo QA-16, 8vo sprint._
- Este proyecto consiste en comprobar la funcionalidad de Urban Routes, donde se llevan a cabo una serie de pruebas automatizadas que cubren el proceso completo de pedir un taxi. 


### **Tecnologías y técnicas utilizadas**: 
- El lenguaje utilizado es _Python_ y la estructura del código se basa en el uso de clases, objetos y métodos haciendo uso del controlador de navegador _Selenium_ donde se emplean
localizadores para acceder a los elementos y métodos específicos para interactuar con la aplicación.
- Se utilizó el Modelo de Objetos de Página para facilitar la organización al momento de las pruebas donde se manejaron los métodos _setup_class()_ y _teardown_class()_.

- El proyecto consta del archivo _data.py_ que contiene los datos para hacer las pruebas y del archivo _main.py_ donde se encuentran los métodos para simular las acciones en la aplicación y las pruebas necesarias para evaluar la funcionalidad en particular. 


### Pruebas
1. En el archivo _data.py_ se encuentran los datos para probar la aplicación. 
Para iniciar, es necesario cambiar la ruta _urban_routes_url_ con la dirección actualizada del servidor.
2. En el archivo _main.py_, cambiar la configuración de ejecución a Pytest. Una vez configurado, ejecutar el script y esperar a que las pruebas terminen.
