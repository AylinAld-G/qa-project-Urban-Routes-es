# Proyecto Urban Routes con Selenium 
## QA-project-Urban-Routes-es
#### _Aldana Guzmán Aylín, grupo QA-16, 8vo sprint._
- Este proyecto consiste en comprobar la funcionalidad de Urban Routes, donde se llevan a cabo una serie de pruebas automatizadas que cubren el proceso completo de pedir un taxi. 


### **Tecnologías y técnicas utilizadas**: 
- El lenguaje utilizado es _Python_ y la estructura del código se basa en el uso de clases, objetos y métodos haciendo uso del controlador de navegador _Selenium_ donde se emplean
localizadores para acceder a los elementos y métodos específicos para interactuar con la aplicación, en los cuales se usan las clases _By_, _WebDriverWait_ y _expected_conditions_.
- Se utilizó el Modelo de Objetos de Página para facilitar la organización al momento de las pruebas donde se manejaron los métodos _setup_class()_ y _teardown_class()_.

- El proyecto consta del archivo _data.py_ que contiene los datos para hacer las pruebas, el archivo _main.py_ donde se encuentran los localizadores y los métodos para simular las acciones en la aplicación, _phone_code.py_ que contiene la función para recuperar el código de verificación del número de teléfono y _TestUrbanRoutes.py_ en el que se realizan las pruebas necesarias para evaluar la funcionalidad en particular.

#### Instalación de Selenium
```sh
pip install selenium
```

### Pruebas
1. En el archivo _data.py_ se encuentran los datos para probar la aplicación. 
Para iniciar, es necesario cambiar la ruta _urban_routes_url_ con la dirección actualizada del servidor.
2. Dentro del archivo _main.py_ asegurarse de importar las librerías _common_ y _support_ y el archivo _phone_code_:
   ```sh
   from selenium.webdriver.support import expected_conditions as EC
   from selenium.webdriver.support.wait import WebDriverWait
   from selenium.webdriver.common.by import By
   from phone_code import retrieve_phone_code
   ```
3. En el archivo _TestUrbanRoutes.py_, importar la clase webdriver:
  ```sh
  from selenium import webdriver y los archivos _data_ y _main_
  import data
  from main import UrbanRoutesPage
  ```
   - Cambiar la configuración de ejecución a Pytest. Una vez configurado, ejecutar el script con el comando _pytest TestUrbanRoutes.py_ en la terminal y esperar a que las pruebas terminen.
