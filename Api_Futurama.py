import matplotlib.pyplot as plt
import requests
import json

response = requests.get("https://api.sampleapis.com/futurama/characters")
personajes = response.json()

# 1. Agrupar en listas por género a los personajes.
# Crear diccionarios para cada género
personajes_masculinos = []
personajes_femeninos = []
otros_personajes = []

for personaje in personajes:
    nombre_completo = f"{personaje['name']['first']} {personaje['name']['middle']} {personaje['name']['last']}"

    if personaje["gender"].lower() == "male":
        personajes_masculinos.append(nombre_completo)
    elif personaje["gender"].lower() == "female":
        personajes_femeninos.append(nombre_completo)
    else:
        otros_personajes.append(nombre_completo)

print(personajes_masculinos)
print(personajes_femeninos)

# 2. A partir de las especies que aparecen en las listas construidas en el punto anterior, haga el respectivo diagrama de barras de especies.
contador_especies = {}

for personaje in personajes:
    especies = personaje['species']
    contador_especies[especies] = contador_especies.get(especies, 0) + 1

# Preparar datos para el diagrama de barras
especies = list(contador_especies.keys())
cantidades = list(contador_especies.values())

# Crear el diagrama de barras
plt.figure(figsize=(10, 6))
plt.bar(especies, cantidades, color='skyblue')
plt.xlabel('Especies')
plt.ylabel('Cantidad')
plt.title('Cantidad de cada especie')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Haga un diagrama de sectores (pie, torta .....) de las especies sin la agrupación por género.
# Reutilizar los datos de especies y cantidades obtenidos en el punto anterior

# Crear el diagrama de sectores
plt.pie(cantidades, labels=especies, autopct='%1.1f%%')
plt.title('Distribución de especies')
plt.show()

# 4. Hacer un histograma de las edades por listado de géneros
edades_masculinos = []
edades_femeninos = []

for personaje in personajes:
    edad = personaje["age"]

    if personaje["gender"].lower() == "male":
        if edad == "Unknown":
            edades_masculinos.append(1025)
        else:
            edades_masculinos.append(int(edad))
    elif personaje["gender"].lower() == "female":
        if edad == "Unknown":
            edades_femeninos.append(1025)
        else:
            edades_femeninos.append(int(edad))

# Ordenar las listas de edades
edades_masculinos.sort()
edades_femeninos.sort()

# Crear y mostrar el histograma de edades para masculinos
plt.hist(edades_masculinos, color='skyblue', edgecolor='black')
plt.xlabel('Edades')
plt.ylabel('Frecuencia')
plt.title('Histograma de Edades de Personajes Masculinos')
plt.grid(True)
plt.show()

# Crear y mostrar el histograma de edades para femeninos
plt.hist(edades_femeninos, color='skyblue', edgecolor='black')
plt.xlabel('Edades')
plt.ylabel('Frecuencia')
plt.title('Histograma de Edades de Personajes Femeninos')
plt.grid(True)
plt.show()

# 5. Haga un histograma de las edades sin la agrupación por género.
edades = []

for personaje in personajes:
    edad = personaje["age"]

    if edad == "Unknown":
        edades.append(1025)
    else:
        edades.append(int(edad))

# Ordenar la lista de edades
edades.sort()

# Crear y mostrar el histograma de edades sin agrupación por género
plt.hist(edades, color='skyblue', edgecolor='black')
plt.xlabel('Edades')
plt.ylabel('Frecuencia')
plt.title('Histograma de Edades de Personajes')
plt.grid(True)
plt.show()

# 6. Agrupar los nombres completos de los personajes en una lista e imprimirla
nombres_completos = []

for personaje in personajes:
    nombre_completo = f"{personaje['name']['first']} {personaje['name']['middle']} {personaje['name']['last']}"
    nombres_completos.append(nombre_completo)

print(nombres_completos)
