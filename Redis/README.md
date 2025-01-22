Requisitos del Entorno
Sistema Operativo
Ubuntu 20.04 (u otra distribución Linux compatible).
Software Necesario
Redis (Servidor y cliente)

Instalación:
sudo apt update
sudo apt install redis-server -y

Configuración opcional para habilitar persistencia (modificar /etc/redis/redis.conf):
appendonly yes

Reinicia Redis para aplicar cambios:
sudo systemctl restart redis
Verifica que Redis está funcionando:
redis-cli ping
Deberías recibir PONG.

Python 3
Instalación:
sudo apt install python3 python3-pip -y

Instalar la librería redis-py
Usa pip para instalar la librería:

pip3 install redis

Estructura del Proyecto
El proyecto contiene los siguientes archivos:
├── create_test.py        # Prueba de inserción masiva
├── read_test.py          # Prueba de lectura por clave
├── update_test.py        # Prueba de actualización masiva
├── delete_test.py        # Prueba de eliminación masiva
├── Makefile              # Script para ejecutar todas las pruebas
├── README.md             # Documentación del proyecto

Cómo Ejecutar las Pruebas
1. Clona el repositorio
bash
Copy
Edit
git clone https://github.com/Felipe-V13/Lab2_DB
Luego acceder con el comando cd a la carpetda llamada Redis

2. Puedes ejecutar cada prueba manualmente con Python:
python3 create_test.py
python3 read_test.py
python3 update_test.py
python3 delete_test.py

3. Ejecuta todas las pruebas con Make
Usa el Makefile para ejecutar todas las pruebas en orden:

make all

Resultados Esperados
Cada prueba muestra el tiempo total requerido para completar la operación en 10,000 registros.