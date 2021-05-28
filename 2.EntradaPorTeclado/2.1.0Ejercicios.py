# -*- coding: utf-8 -*-

#%%SOLUCION CUADRATICA
# Realizar un programa que haga el proceso de formula general para la resolución 
# de ecuaciones, sabiendo que la formula general es la que está en la imagen, el
#  usuario debe ingresar los valores de “a”, “b” y “c”, y el programa debe hacer 
#  el proceso para que al final muestre el mensaje: “La solución es: <solucion>”

import math

a = int(input('Ingrese Variable a: '))
b = int(input('Ingrese variable b: '))
c = int(input('Ingrese variable c: '))

#Soluciones

Cuadrada = math.sqrt((b**2)-(4*a*c))

X1 = (-b + Cuadrada)/(2*a)
X2 = (-b - (math.sqrt(pow(b,2)-(4*a*c))))/(2*a)

X23 = (-b - (math.sqrt(b**2-(4*a*c))))/(2*a)

print('La solución Positiva es: ', X1)
print('La solución negativa es: ', X2)

print('La solución negativa es: ', X23)

#Sol Profe
from math import sqrt

a1 = int(input('Ingrese Variable a: '))
b1 = int(input('Ingrese variable b: '))
c1 = int(input('Ingrese variable c: '))

X11 = 0
X21 = 0

if ((b1**2)-(4*a*c))<0:
    print('No se puede Resolver')
else:

     X11 = (-b1 + sqrt((b1**2)-(4*a1*c1)))/(2*a1)  
     X21 = (-b1 - sqrt((b1**2)-(4*a1*c1)))/(2*a1)    

     print('La Solucion es: \n X1= ', X11,'\n X2= ',X21)

#%%PROMEDIO

# Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha 
# obtenido un alumno en un determinado curso, conociendo las notas de: tres 
# prácticas, el examen parcial y el examen final.

# Considere:

# PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6

# Donde: P1, P2, P3 : Practicas

# PP: promedio de práctica

# PROM: promedio

# EP: examen parcial

# EF: examen final

P1 = float(input('Nota Primera Prueba: '))
P2 = float(input('Nota Segunda Prueba: '))
P3 = float(input('Nota Tercera Prueba: '))
EP = float(input('Nota Exaamen Parcial: '))
EF = float(input('Nota Examen Final: '))

PP = (P1 + P2 + P3)/3
PROM = (PP + 2*EP + 3*EF)/6

print('Tu Promedio de Práctica es: ', PP)
print('Tu Promedio es: ', PROM)