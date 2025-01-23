import redis
import time

# Conexión a Redis
r = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

# Prueba de eliminación masiva
def delete_records():
    start_time = time.time()  # Inicio del temporizador
    for i in range(10000):
        r.delete(f"key{i}")  # Eliminación por clave
    end_time = time.time()  # Fin del temporizador

    print(f"Tiempo total para eliminar 10,000 registros: {end_time - start_time:.2f} segundos")

if __name__ == "__main__":
    delete_records()
