# -*- coding: utf-8 -*-

Diccionario = {1: "Juanito Espinacas", 2: "Pepa Cerdo", 3: "Camila del Carmen"}

print(type(Diccionario))
print(Diccionario)
print(Diccionario[3])
print(Diccionario[1])
print(2 in Diccionario)

Value = Diccionario.values() # convierte un diccionario en lista
print('Pepa Cerdo' in Value)
