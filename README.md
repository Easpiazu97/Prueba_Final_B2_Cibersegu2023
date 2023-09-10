# Servicio Web Python con Flask y MongoDB Atlas
Este repositorio contiene un servicio web básico desarrollado en Python utilizando el framework Flask para acceder a una base de datos MongoDB alojada en MongoDB Atlas y presentar los datos en la consola.

## Requisitos Previos
Asegúrate de tener los siguientes requisitos previos configurados antes de ejecutar el servicio web:
- **Python:** Debes tener Python 3.x instalado en tu sistema. Si no lo tienes instalado, puedes descargarlo desde [Python.org](https://www.python.org/downloads/).
- **Flask:** Instala Flask utilizando pip:
`pip install Flask`
- **PyMongo:** Instala PyMongo para conectar tu aplicación Flask a MongoDB:
`pip install pymongo`
 - **MongoDB Atlas:** Crea una cuenta en MongoDB Atlas si aún no tienes una. Luego, crea un clúster de MongoDB y configura una base de datos.
- **URI de Conexión de MongoDB Atlas:** Obtén la cadena de conexión de tu clúster de MongoDB Atlas.

## Configuración
- **Clona este repositorio en tu sistema local:**
`git clone https://github.com/tu-usuario/Prueba_Final_B2_Cibersegu2023.git
cd Prueba_Final_B2_Cibersegu2023`

## Ejecución
Para ejecutar el servicio web, utiliza el siguiente comando:
`python api.py`
El servicio se ejecutará en http://localhost:5000/.

## Uso
Accede a la URL http://localhost:5000/ en tu navegador o utilizando herramientas como cURL o Postman para interactuar con el servicio web. Este servicio web recupera datos de la base de datos MongoDB y muestra un print de los datos en la consola.

## Contribuciones
Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

- Realiza un fork del repositorio.
Crea una nueva rama (**git checkout -b feature/nueva-caracteristica**).
- Realiza tus cambios y haz commit (**git commit -m 'Añadir nueva característica'**).
- Sube tus cambios a tu repositorio fork (**git push origin feature/nueva-caracteristica**).
- Crea una solicitud de extracción en este repositorio.

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más detalles.

¡Gracias por usar este servicio web!
