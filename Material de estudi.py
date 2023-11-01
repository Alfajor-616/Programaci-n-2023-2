# La función map(), filter(), reduce(), zip() y Lambda() en Python

# map()
# Esta función aplica una función sobre todos los elementos y como resultado se devuelve un iterable de tipo map
# La función map() aplica una función a cada elemento de un iterable.

# convertir numeros/strings en flotantes
from functools import reduce
numbers = [3, '23', 42]
print(list(map(float, numbers)))

# multiplicar por dos


def doblar(numero):
    return numero * 2


numeros = [2, 5, 10, 23, 50, 33]

# si no se le da el parametro de lista retornara algo asi <map object at 0x000001DB5C085BA0>
print(map(doblar, numeros))
# improtante ponerle el list para retornar una lista y no un objeto de tipo map
print(list(map(doblar, numeros)))

# Filter()
# La función filter() crea una nueva lista con los elementos que cumplen cierta condición.


def multiple(numero):    # Primero declaramos una función condicional
    if numero % 5 == 0:  # Comprobamos si un numero es múltiple de cinco
        return True      # Sólo devolvemos True si lo es


numeros = [2, 5, 10, 23, 50, 33]

# si no se le da el parametro de lista retornara algo asi <filter object at 0x000001DB5C085BA0>
print(filter(multiple, numeros))
# improtante ponerle el list para retornar una lista y no un objeto de tipo filtor
print(list(filter(multiple, numeros)))

# Filtrando objetos

# Por ejemplo, dada una lista con varias personas, nos gustaría filtrar únicamente las que son menores de edad:

'''
El código crea una clase llamada "Persona" con atributos de nombre y edad.
Luego, se crea una lista de objetos de la clase Persona.
Se filtran los elementos de la lista que representan personas menores de 18 años.
Finalmente, se imprime cada persona menor de edad.
'''


class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "{} de {} años".format(self.nombre, self.edad)


personas = [Persona("Juan", 35), Persona("Marta", 16),
            Persona("Manuel", 78), Persona("Eduardo", 12)]

menores = filter(lambda persona: persona.edad < 18, personas)

for menor in menores:
    print(menor)

# Reduce()
'''
reduce() es una función incorporada muy útil, puede ejecutar el cálculo de objetos iterables y devolver el resultado, 
puede calcular de forma continua los valores continuos en una secuencia iterable, esto para reducir el numero de items,
como el producto acumulativo de una lista de enteros o la suma acumulativa.

'''


def do_sum(num1, num2):
    return num1 + num2


print(f"The sum of 1, 2, 3, 4 is: {reduce(do_sum, [1, 2, 3, 4])}.")


# Zip()
# Como su nombre lo indica, la función zip() es juntar varios objetos iterables y "empaquetarlos" como un solo objeto, mapeándolos con un índice similar.

keys = ['name', 'age']
values = ['Apple', '44']

apple_dict = dict(zip(keys, values))
print(apple_dict)

names = ['Apple', 'Google', 'Microsoft']
ages = ['44', '21', '44']
values = ['100', '80', '60']

mapped_values = list(zip(names, ages, values))
print(mapped_values)

# lambda()

'''
Mientras que las funciones normales se definen utilizando la palabra clave def, en Python las funciones 
anónimas se definen utilizando la palabra clave lambda. Por lo tanto, las funciones anónimas también se denominan funciones lambda.
La función Lambda puede usar cualquier cantidad de parámetro, pero solo tiene una expresión:
'''

university = [{'name': 'NYU',
               'city': 'New York'},
              {'name': 'NUS',
               'city': "Singapore"}]

names = list(map(lambda x: x['name'], university))
print(names)

name = list(filter(lambda x: x['name'] == 'NUS', university))
print(names)
