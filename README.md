# Proyecto MongoDB - Pruebas de Rendimiento

Este proyecto evalúa el rendimiento de MongoDB para realizar operaciones comunes en bases de datos NoSQL, como la inserción masiva de datos, consultas, actualizaciones y eliminaciones bajo condiciones controladas.

## 1. Descripción Detallada del Proceso de Instalación y Preparación del Entorno

### Instalación de MongoDB

#### Descarga:
1. Descargar MongoDB desde la página oficial: [MongoDB Downloads](https://www.mongodb.com/try/download/community).

#### Instalación en Windows:
1. Ejecutar el instalador descargado y seguir las instrucciones de instalación.
2. Seleccionar la opción "Complete" durante la instalación.
3. Añadir MongoDB al PATH del sistema para poder ejecutar el comando `mongod` desde la terminal.

#### Verificación:
1. Después de la instalación, verificar que MongoDB esté funcionando correctamente ejecutando el comando:
   ```bash
   mongod
Esto iniciará el servidor de MongoDB. 2. Verificar la conexión ejecutando el siguiente comando en la terminal:

bash
Copiar
Editar
mongo
Esto abrirá la shell interactiva de MongoDB.

Preparación del Entorno de Desarrollo
Instalar Python y Dependencias:
Crear un entorno virtual utilizando el siguiente comando:
bash
Copiar
Editar
python -m venv .venv
Instalar las bibliotecas necesarias, como pymongo para interactuar con MongoDB:
bash
Copiar
Editar
pip install pymongo
Conexión a MongoDB:
Crear un archivo de Python y conectar con MongoDB usando el siguiente código:
python
Copiar
Editar
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['LAB2_DB']
collection = db['LAB2_DB']
Verificación del Entorno:
Insertar, actualizar, leer y eliminar datos de prueba para verificar que el entorno está correctamente configurado.
2. Diseño del Experimento y Metodología de Evaluación
Objetivo del Experimento:
Evaluar el rendimiento de MongoDB para manejar operaciones comunes como inserción masiva de datos, consultas, actualizaciones y eliminaciones bajo condiciones controladas.

Pruebas Implementadas:
Create (Inserción Masiva): Insertar un mínimo de 10,000 registros en la base de datos.
Read (Consulta): Realizar consultas por clave primaria (user_id), y filtros de búsqueda como email, name y age.
Update (Actualización Masiva): Actualizar registros que cumplan con una condición específica (por ejemplo, cambiar el campo premium_member para usuarios mayores de 30 años).
Delete (Eliminación Masiva): Eliminar registros que cumplan con una condición (por ejemplo, eliminar usuarios con age < 25).
Medición de Rendimiento:
Se mide el tiempo que toma cada operación utilizando la función time.time().
3. Análisis de Resultados, Incluyendo Gráficos y Tablas Comparativas
Resultados de las Pruebas de Rendimiento
A continuación se presentan los tiempos de ejecución de cada operación (Create, Read, Update, Delete) en MongoDB.

Tabla de Resultados de Tiempo de Ejecución:
Operación	Tiempo de Ejecución (segundos)
Create	0.04
Read	0.05
Update	0.05
Delete	0.05
