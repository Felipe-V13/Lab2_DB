import redis
import time

# Conexión a Redis
r = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

# Prueba de actualización masiva
def update_records():
    start_time = time.time()  # Inicio del temporizador
    for i in range(10000):
        r.set(f"key{i}", f"updated_value{i}")  # Actualización clave-valor
    end_time = time.time()  # Fin del temporizador

    print(f"Tiempo total para actualizar 10,000 registros: {end_time - start_time:.2f} segundos")

if __name__ == "__main__":
    update_records()
