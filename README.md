# Proyecto Urban Routes con Selenium 
## QA-project-Urban-Routes-es
#### _Aldana Guzmán Aylín, grupo QA-16, 8vo sprint._
- Este proyecto consiste en comprobar la funcionalidad de Urban Routes, donde se llevan a cabo una serie de pruebas automatizadas que cubren el proceso completo de pedir un taxi. 


### **Tecnologías y técnicas utilizadas**: 
- El lenguaje utilizado es _Python_ y la estructura del código se basa en el uso de clases, objetos y métodos haciendo uso del controlador de navegador _Selenium_ donde se emplean
localizadores para acceder a los elementos y métodos específicos para interactuar con la aplicación, en los cuales se usan las clases _By_, _WebDriverWait_ y _expected_conditions_.
- Se utilizó el Modelo de Objetos de Página para facilitar la organización al momento de las pruebas donde se manejaron los métodos _setup_class()_ y _teardown_class()_.

#### Archivo _data.py_
Contiene los datos para hacer las pruebas.

![dat](https://github.com/user-attachments/assets/d4098f11-0652-4c42-ad47-d95cbf1da49a)


#### Archivo _main.py_
En él se encuentran los localizadores y los métodos para simular las acciones en la aplicación.
##### Localizadores
![loc1](https://github.com/user-attachments/assets/7e9a0db3-106b-4e32-a434-973af94de0ff)

![loc2](https://github.com/user-attachments/assets/ba326e25-ec56-4bb5-9eab-9976b51d7d61)

##### Métodos
![met1](https://github.com/user-attachments/assets/e82a3fa8-d451-4a67-a612-d8b6bc9ac4f4)

![met2](https://github.com/user-attachments/assets/8becb4ff-2456-4302-ae62-8e0979c786a2)

![met3](https://github.com/user-attachments/assets/e46706a4-afa0-42e4-bcc9-a881bce6babe)

![met4](https://github.com/user-attachments/assets/158635f2-a291-438d-9251-ee88955c885e)

![met5](https://github.com/user-attachments/assets/641ce3fd-090c-4468-9d72-78013d20002f)

![met6](https://github.com/user-attachments/assets/faed7a7b-b548-4dca-b58c-ab72e1cac1fb)

![met7](https://github.com/user-attachments/assets/f75dac18-1f0d-49fa-873b-8ba63f657d53)

![met8](https://github.com/user-attachments/assets/22426f0e-482f-4fa5-bc0a-a0efaa9b0094)


**Pasos**

![met9](https://github.com/user-attachments/assets/4611239c-4042-4067-aeb9-c07061099b89)



#### Archivo _phone_code.py_
Contiene la función para recuperar el código de verificación del número de teléfono.

![retrieve](https://github.com/user-attachments/assets/8ff09828-5d9e-4f49-a6ab-f72d7d4e76ab)



#### Archivo _TestUrbanRoutes.py_ 
Dentro de él se realizan las pruebas necesarias para evaluar la funcionalidad en particular.

##### Clase setup
![setupclass](https://github.com/user-attachments/assets/67d719ab-0b89-4013-b82c-64ff83a184dd)

##### Pruebas
![test1](https://github.com/user-attachments/assets/2f3ef82b-fb40-4d94-9299-f492a99fb84d)

![test2](https://github.com/user-attachments/assets/0ef98457-29b9-4922-a869-7d1b73dba8b9)

![test3](https://github.com/user-attachments/assets/f1d1e093-2396-4007-ad3f-e4b46b7ea1fa)


##### Clase teardown
![teardown](https://github.com/user-attachments/assets/2330a6e0-a490-49bc-bbd6-c436df7cd165)

### Comandos de instalación e importaciones


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
     ![runtest](https://github.com/user-attachments/assets/a1c181b5-bd49-4821-aa5e-9a78e6cc92de)

