# Proyecto MongoDB - Pruebas de Rendimiento

Este proyecto evalúa el rendimiento de MongoDB para realizar operaciones comunes en bases de datos NoSQL, como la inserción masiva de datos, consultas, actualizaciones y eliminaciones bajo condiciones controladas.

## 1. Instalación y Preparación del Entorno

### 1.1 Instalación de MongoDB

#### 1.1.1 Descarga

1. Descargar MongoDB Community Server desde la página oficial: [MongoDB Downloads](https://www.mongodb.com/try/download/community). Seleccionar la versión y el sistema operativo adecuados.

#### 1.1.2 Instalación en Windows

1. Ejecutar el instalador descargado (`.msi`) y seguir las instrucciones.
2. Se recomienda una instalación "Complete".
3. **Importante:** Durante la instalación, se ofrece la opción de instalar MongoDB Compass. Es una herramienta GUI útil para administrar MongoDB, se recomienda instalarla.
4. Añadir el directorio `bin` de MongoDB al PATH del sistema. La ruta típica es `C:\Program Files\MongoDB\Server\<versión>\bin`. Esto permite ejecutar `mongod` y `mongo` desde cualquier terminal.

#### 1.1.3 Verificación de la Instalación (Servidor MongoDB)

1. Abrir una nueva terminal (para que los cambios en el PATH surtan efecto).
2. Ejecutar `mongod`. Esto iniciará el servidor de MongoDB en el puerto 27017 por defecto. Deberías ver mensajes en la terminal indicando que el servidor se está iniciando. **No cierres esta terminal mientras trabajas con MongoDB.**
3. **Nueva Terminal (Cliente MongoDB):** Abrir *otra* terminal y ejecutar `mongo`. Esto abrirá la shell interactiva de MongoDB, conectándose al servidor que se está ejecutando. Si se conecta correctamente, verás el prompt `>`. Prueba ejecutar algunos comandos básicos como `show dbs` para listar las bases de datos.
4. Para detener el servidor MongoDB, regresa a la terminal donde ejecutaste `mongod` y presiona `Ctrl+C`.

### 1.2 Preparación del Entorno de Desarrollo Python

#### 1.2.1 Instalación de Python y Dependencias

1. Asegúrate de tener Python instalado. Se recomienda Python 3.7 o superior.
2. Crear un entorno virtual:
    ```bash
    python -m venv .venv  # En Windows
    python3 -m venv .venv # En macOS/Linux
    ```
3. Activar el entorno virtual:
    ```bash
    .venv\Scripts\activate  # En Windows
    source .venv/bin/activate # En macOS/Linux
    ```
4. Instalar la biblioteca `pymongo`:
    ```bash
    pip install pymongo
    ```

#### 1.2.2 Conexión a MongoDB con Python

1. Crear un archivo Python (ej. `main.py`).
2. Añadir el siguiente código para conectar a MongoDB:

    ```python
    from pymongo import MongoClient

    try:
        client = MongoClient('mongodb://localhost:27017/') # Conexión local
        db = client['LAB2_DB'] # Selecciona o crea la base de datos
        collection = db['datos_prueba'] # Selecciona o crea la colección
        print("Conexión a MongoDB exitosa")
        # Ejemplo de inserción para verificar la conexión
        collection.insert_one({"test":"test"})
        print("Inserción de prueba exitosa")
        # NO es necesario borrar la base de datos aquí. Se borrará al final de las pruebas.
        # client.drop_database("LAB2_DB") 
    except Exception as e:
        print(f"Error al conectar a MongoDB: {e}")
    finally:
        client.close() # Cierra la conexión
        print("Conexión cerrada")
    ```

#### 1.2.3 Verificación del Entorno Python

Ejecutar el script `main.py`. Si se imprime "Conexión a MongoDB exitosa" y "Inserción de prueba exitosa" en la consola, el entorno está configurado correctamente.

#### 1.3 Solución de Problemas de Conexión (MongoDB Compass y Terminal)

Si tienes problemas para conectar a MongoDB, sigue estos pasos:

1. **Asegúrate de que `mongod` se esté ejecutando:** Abre una terminal y ejecuta `mongod`. Debes ver mensajes indicando que el servidor se está iniciando. Si no se está ejecutando, la conexión fallará.

2. **Conexión explícita con `mongo`:** Si la conexión con `mongo` (solo `mongo` en la terminal) falla, intenta especificar el host y el puerto:

    ```bash
    mongo --host localhost --port 27017
    ```
**Ejecutar `mongod` con `--dbpath`:** Este es el paso crucial para iniciar el servidor y especificar la ruta de los datos. **Si no se especifica `--dbpath`, MongoDB intentará usar una ruta por defecto que podría no existir, generando errores.**

   ```bash
   .\mongod.exe --dbpath="C:\data\db"
 ```
3. **Verificar la ruta de MongoDB:** Asegúrate de que la ruta al directorio `bin` de MongoDB esté correctamente añadida al PATH del sistema.

4. **MongoDB Compass:**
    * Abre MongoDB Compass.
    * En el campo de conexión, asegúrate de que esté configurado como `mongodb://localhost:27017`.
    * Si la conexión falla, revisa los logs de MongoDB (la terminal donde se ejecuta `mongod`) para buscar mensajes de error.
    * Si sigues teniendo problemas, intenta la conexión desde la terminal con `mongo --host localhost --port 27017` primero, y luego intenta conectar desde Compass. Esto a veces ayuda a "desbloquear" la conexión.


## 2. Diseño del Experimento y Metodología de Evaluación

### 2.1 Objetivo del Experimento

Evaluar el rendimiento de MongoDB en operaciones CRUD (Create, Read, Update, Delete) bajo condiciones controladas, midiendo el tiempo de ejecución de cada operación.

### 2.2 Pruebas Implementadas

*   **Create (Inserción Masiva):** Insertar un número significativo de documentos (ej. 100,000 o más para obtener resultados más representativos) en la colección.
*   **Read (Consulta):**
    *   Consultas por `_id` (clave primaria).
    *   Consultas por campos indexados (ej. `email`, `name`).
    *   Consultas con filtros (ej. `age` mayor que un valor).
*   **Update (Actualización Masiva):** Actualizar un subconjunto de documentos que cumplan con un criterio específico (ej. actualizar el campo `premium_member` para usuarios mayores de 30).
*   **Delete (Eliminación Masiva):** Eliminar documentos que cumplan con una condición (ej. eliminar usuarios con `age` menor que 25).

### 2.3 Medición de Rendimiento

Utilizar el módulo `time` de Python para medir el tiempo de ejecución de cada operación:

```python
import time

start_time = time.time()
# Código de la operación a medir
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Tiempo de ejecución: {elapsed_time} segundos")
