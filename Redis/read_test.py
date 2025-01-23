import redis
import time

# Conexión a Redis
r = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

# Prueba de lectura por clave
def read_records():
    start_time = time.time()  # Inicio del temporizador
    for i in range(10000):
        _ = r.get(f"key{i}")  # Consulta de cada clave
    end_time = time.time()  # Fin del temporizador

    print(f"Tiempo total para leer 10,000 registros: {end_time - start_time:.2f} segundos")

if __name__ == "__main__":
    read_records()
