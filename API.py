# para guardar el proceso de mi codigo en github se hacen los siguientes pasos desde la terminal:
# git add .
# git commit -m "cambio"
# git log --oneline
# git push

# 1. Agrupar en listas por género a los personajes.
# 2. A partir de las especies que aparecen en las listas construidas en el punto anterior, haga el respectivo diagrama de barras de especies.
# 3. Haga un diagrama de sectores (pie, torta .....) de las especies sin la agrupación por género.
# 4. Hacer un histograma de las edades por listado de géneros
# 5. Haga un histograma de las edades sin la agrupación por género.
# 6. Agrupar los nombres completos de los personajes en una lista e imprimirla
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

# Iterar a través de los personajes y clasificarlos por género
for personaje in personajes:
    if personaje["gender"].lower() == "male":
        personajes_masculinos.append(
            f"{personaje['name']['first']} {personaje['name']['middle']} {personaje['name']['last']}")

    elif personaje["gender"].lower() == "female":
        personajes_femeninos.append(
            f"{personaje['name']['first']} {personaje['name']['middle']} {personaje['name']['last']}")
    else:
        otros_personajes.append(
            f"{personaje['name']['first']} {personaje['name']['middle']} {personaje['name']['last']}")

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
plt.xticks(rotation=45)  # Rotar etiquetas del eje x para mayor claridad
plt.tight_layout()  # Ajustar el diseño para evitar cortar las etiquetas
plt.show()

# 3. Haga un diagrama de sectores (pie, torta .....) de las especies sin la agrupación por género.

especies = list(contador_especies.keys())
cantidades = list(contador_especies.values())

# Create a figure and an axes.
fig, ax = plt.subplots()

# Create the data for the pie chart.
labels = especies
sizes = cantidades

# Draw the pie chart.
ax.pie(sizes, labels=labels, autopct='%1.1f%%')

# Show the pie chart.
plt.show()

# 4. Hacer un histograma de las edades por listado de géneros

edades_masculinos = []
edades_femeninos = []

for personaje in personajes:

    if personaje["gender"].lower() == "male":
        if personaje['age'] == "Unknown":
            edades_masculinos.append('1025')

        else:
            edades_masculinos.append(personaje["age"])

    elif personaje["gender"].lower() == "female":
        if personaje['age'] == "Unknown":
            edades_femeninos.append('1025')

        else:
            edades_femeninos.append(personaje["age"])
# Convierte las cadenas de texto a enteros
edades_masculinos = [int(edad) for edad in edades_masculinos]
edades_masculinos.sort()  # Ordena la lista de menor a mayor

plt.hist(edades_masculinos, color='skyblue', edgecolor='black')
plt.xlabel('Edades')
plt.ylabel('Frecuencia')
plt.title('Histograma de Edades de Personajes')
plt.grid(True)
plt.show()

edades_femeninos = [int(edad) for edad in edades_femeninos]
edades_femeninos.sort()

plt.hist(edades_femeninos, color='skyblue', edgecolor='black')
plt.xlabel('Edades')
plt.ylabel('Frecuencia')
plt.title('Histograma de Edades de Personajes')
plt.grid(True)
plt.show()

# 5. Haga un histograma de las edades sin la agrupación por género.
edades = []
for personaje in personajes:
    if personaje['age'] == "Unknown":
        edades.append('1025')

    else:
        edades.append(personaje["age"])

# Convierte las cadenas de texto a enteros
edades = [int(edad) for edad in edades]
edades.sort()  # Ordena la lista de menor a mayor

print(edades)

# Crear un histograma
plt.figure(figsize=(8, 6))
# Puedes ajustar el número de contenedores (bins) según tus necesidades
plt.hist(edades, color='skyblue', edgecolor='black')
plt.xlabel('Edades')
plt.ylabel('Frecuencia')
plt.title('Histograma de Edades de Personajes')
plt.grid(True)
plt.show()

# 6. Agrupar los nombres completos de los personajes en una lista e imprimirla
nombres_completos = []

for personaje in personajes:
    nombres_completos.append(
        f"{personaje['name']['first']} {personaje['name']['middle']} {personaje['name']['last']}")

print(nombres_completos)
