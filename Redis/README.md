# Requisitos del Entorno

### Sistema Operativo
- Ubuntu 20.04 (u otra distribución Linux compatible).

### Software Necesario
- Redis (Servidor y cliente).

Instalación:
```bash
sudo apt update
sudo apt install redis-server -y
```

Configuración opcional para habilitar persistencia (modificar el archivo `/etc/redis/redis.conf`):
```bash
appendonly yes
```

Reinicia Redis para aplicar los cambios:
```bash
sudo systemctl restart redis
```

Verifica que Redis está funcionando:
```bash
redis-cli ping
```
Deberías recibir como respuesta:
```bash
PONG
```

### Python 3

Instalación:
```bash
sudo apt install python3 python3-pip -y
```

Instalar la librería `redis-py`:
```bash
pip3 install redis
```

---

# Estructura del Proyecto

El proyecto contiene los siguientes archivos:
```
├── create_test.py   # Prueba de inserción masiva
├── read_test.py     # Prueba de lectura por clave
├── update_test.py   # Prueba de actualización masiva
├── delete_test.py   # Prueba de eliminación masiva
├── Makefile         # Script para ejecutar todas las pruebas
├── README.md        # Documentación del proyecto
```

---

# Cómo Ejecutar las Pruebas

### Clona el repositorio
```bash
git clone https://github.com/Felipe-V13/Lab2_DB
```

Accede al directorio del proyecto:
```bash
cd Lab2_DB/Redis
```

### Ejecutar Pruebas Individualmente
Puedes ejecutar cada prueba manualmente con Python:
```bash
python3 create_test.py
python3 read_test.py
python3 update_test.py
python3 delete_test.py
```

### Ejecutar Todas las Pruebas
Usa el `Makefile` para ejecutar todas las pruebas en orden:
```bash
make all
```

---

# Resultados Esperados

Cada prueba muestra el tiempo total requerido para completar la operación en **10,000 registros**. Los resultados serán impresos en la consola después de ejecutar cada prueba.

---

# Notas

- Asegúrate de que el servidor Redis esté en funcionamiento antes de ejecutar las pruebas.
- Puedes personalizar el número de registros modificando los scripts según tus necesidades.

---
