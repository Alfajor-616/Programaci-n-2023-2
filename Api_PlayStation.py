import matplotlib.pyplot as plt
import requests

response = requests.get("https://api.sampleapis.com/playstation/games")
data = response.json()

generos = []
desarrolladores = []
juegos_FromSoftware = {}

for juego in data:
    # agrupar los generos en una lista en la cual no se repitan
    generos.append(str(juego['genre']))

    # agrupar los desarrolladores en una lista en la cual no se repitan
    desarrolladores.append(str(juego['developers']))

    # agrupar los juegos de un desarrolador en concreto
    if juego['developers'] == 'FromSoftware':
        juegos_FromSoftware.append(juego["name"])

lista_generos = list(set(generos))
lista_desarrolladores = list(set(desarrolladores))
lista_juegos_FromSoftware = list(juegos_FromSoftware)

print(lista_generos)
print(lista_desarrolladores)
print(lista_juegos_FromSoftware)
