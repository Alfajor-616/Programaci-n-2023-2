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

if response.status_code == 200:
    # for personaje in personajes:
    #   print(
    #       f"Nombre: {personaje['name']['first']} {personaje['name']['middle']} {personaje['name']['last']}")

    # Crear diccionarios para cada género
    personajes_hombres = []
    personajes_mujeres = []
    otros_personajes = []

    # Iterar a través de los personajes y clasificarlos por género
    for personaje in personajes:
        if personaje["gender"].lower() == "male":
            personajes_hombres.append(personaje)
        elif personaje["gender"].lower() == "female":
            personajes_mujeres.append(personaje)
        else:
            otros_personajes.append(personaje)

    # Imprimir los personajes por género
    print("Personajes masculinos:")
    for personaje in personajes_hombres:
        # Puedes ajustar la impresión según la estructura de datos
        print(personaje["name"]["first"], personaje['name']
              ['middle'], personaje['name']['last'])

    print("\nPersonajes femeninos:")
    for personaje in personajes_mujeres:
        # Puedes ajustar la impresión según la estructura de datos
        print(personaje["name"]["first"], personaje['name']
              ['middle'], personaje['name']['last'])

else:
    print("Error al obtener datos de la API")


contador_especies = {}
for personaje in personajes:
    species = personaje['species']
    contador_especies[species] = contador_especies.get(species, 0) + 1

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
