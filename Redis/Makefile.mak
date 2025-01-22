# Comandos básicos
PYTHON := python3

# Archivos de prueba
CREATE_TEST := create_test.py
READ_TEST := read_test.py
UPDATE_TEST := update_test.py
DELETE_TEST := delete_test.py

# Objetivo para ejecutar la prueba de inserción masiva
create:
	@echo "=== Ejecutando prueba de inserción masiva (Create) ==="
	$(PYTHON) $(CREATE_TEST)

# Objetivo para ejecutar la prueba de lectura
read:
	@echo "=== Ejecutando prueba de lectura (Read) ==="
	$(PYTHON) $(READ_TEST)

# Objetivo para ejecutar la prueba de actualización masiva
update:
	@echo "=== Ejecutando prueba de actualización masiva (Update) ==="
	$(PYTHON) $(UPDATE_TEST)

# Objetivo para ejecutar la prueba de eliminación masiva
delete:
	@echo "=== Ejecutando prueba de eliminación masiva (Delete) ==="
	$(PYTHON) $(DELETE_TEST)

# Ejecutar todas las pruebas en orden
all: create read update delete
	@echo "=== Todas las pruebas completadas ==="

# Limpiar archivos temporales (si hubiera)
clean:
	@echo "No hay archivos temporales que limpiar."
