import csv
import time
from pymongo import MongoClient

# Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["LAB2_DB"]
collection = db["LAB2_DB"]

# Leer el archivo CSV y cargar los documentos
with open("mongo_users_data.csv", "r") as file:
    reader = csv.DictReader(file)  # Usa los encabezados del CSV como claves
    documentos = [row for row in reader]

# Medir el tiempo de inserción (Create)
start_time = time.time()
collection.insert_many(documentos)  # Inserta todos los documentos
end_time = time.time()
print(f"Tiempo de inserción (Create): {end_time - start_time:.2f} segundos")

# Función para consultar por user_id
def consultar_por_user_id(user_id):
    resultado = collection.find({"user_id": user_id})
    for usuario in resultado:
        print(usuario)

# Función para consultar por nombre
def consultar_por_nombre(nombre):
    resultado = collection.find({"name": nombre})
    for usuario in resultado:
        print(usuario)

# Función para consultar por email
def consultar_por_email(email):
    resultado = collection.find({"email": email})
    for usuario in resultado:
        print(usuario)

# Función para consultar por edad exacta
def consultar_por_edad(edad):
    resultado = collection.find({"age": edad})
    for usuario in resultado:
        print(usuario)

# Función para consultar por un rango de edad
def consultar_por_rango_edad(min_edad, max_edad):
    resultado = collection.find({"age": {"$gte": min_edad, "$lte": max_edad}})
    for usuario in resultado:
        print(usuario)

# Medir el tiempo de consulta (Read) por user_id
start_time = time.time()
consultar_por_user_id(1)  # Ejemplo de consulta por user_id = 1
end_time = time.time()
print(f"Tiempo de consulta (Read) por user_id: {end_time - start_time:.2f} segundos")

# Medir el tiempo de actualización (Update)
start_time = time.time()
collection.update_many({"age": {"$gte": 30}}, {"$set": {"premium_member": True}})  # Actualiza a los usuarios mayores de 30 años
end_time = time.time()
print(f"Tiempo de actualización (Update): {end_time - start_time:.2f} segundos")

# Medir el tiempo de eliminación (Delete)
start_time = time.time()
collection.delete_many({"age": {"$lt": 10}})  # Elimina usuarios con edad menor a 25
end_time = time.time()
print(f"Tiempo de eliminación (Delete): {end_time - start_time:.2f} segundos")

# Ejemplo de cómo hacer consultas (Desocmente lo que no quiere usar)
# consultar_por_nombre("Juan")  # Consulta por nombre
consultar_por_email("user3@testmail.com")  # Consulta por email
# consultar_por_edad(33)  # Consulta por edad exacta
# consultar_por_rango_edad(20, 40)  # Consulta por rango de edad
