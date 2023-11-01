import requests
# 1)
lista = [1, 2, 3, 4, 5]
lista_cuadrados = [x**2 for x in lista]
print(lista_cuadrados)

# Resultado: [1, 4, 9, 16, 25]

# 2)
nombre = ["Juan", "Ana", "Pedro", "Luisa"]
lista_nombres = list(filter(lambda nombre: len(nombre) > 4, nombre))
print(lista_nombres)

# Resultado: ['Juan', 'Ana']

# 3)
celsius = [0, 20, 25, 30, 35]
Fahrenheit = list(map(lambda n: (n * (9/5)) + 32, celsius))
print(Fahrenheit)

# Resultado: [32.0, 68.0, 77.0, 86.0, 95.0]

# 4)
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_pares = [n for n in lista if n % 2 == 0]
lista_pares1 = list(filter(lambda x: x % 2 == 0, lista))
print(lista_pares)
print(lista_pares1)

# Resultado: [2, 4, 6, 8, 10]

# 5)

Palabras = ["casa", "coche", "perro", "gato"]
Palabras_c = list(filter(lambda palabra: 'c' in palabra, Palabras))
print(Palabras_c)

# Resultado: ['casa', 'coche']

# 6)
lista_nombres = ["Pablo", "Pedro", "Jonata", "Jose"]
nombres = list(filter(lambda nombre: len(nombre) == 4, lista_nombres))
print(nombres)

# Resultado: ['Jose']

# 7)

response = requests.get("http://10.203.1.15:8000/")
data = response.json()
print(type(data))

sedes = set()
if isinstance(data, dict):
    for unal in data:
        if isinstance(unal, dict) and "Sede Andina" in unal:
            sedes.add(str(unal["Sede Andina"]))

lista_sedes = list(sedes)
print(lista_sedes)
