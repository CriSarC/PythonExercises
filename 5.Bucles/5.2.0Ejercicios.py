#%%Ejercicio 1

# Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario dos numeros 
# y mostrar el rango de numeros entre ambas cifras

Numeros = [1,2,3,4,5,6,7,8,9,10]

for i in Numeros:
    print(i)

Rango1 = int(input('ingrese Rango menor: '))
Rango2 = int(input('ingrese Rango mayor: '))

for Numeros in range(Rango1+1,Rango2):
    print(Numeros)

#%%Ejercicio 2

# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

Palabra = input('ingrese una palabra: ')

for i in range(0,10):
    print(Palabra)